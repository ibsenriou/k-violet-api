import os
import json
from datetime import date, timedelta
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from src.core.models import DailyMission

class Command(BaseCommand):
    help = "Generate weekly task fixtures for a given user"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str, help="Email of the user to generate tasks for")

    def handle(self, *args, **kwargs):
        user_email = kwargs["email"]

        # Fetch the user
        User = get_user_model()
        try:
            user = User.objects.get(email=user_email)
            user_id = str(user.id)  # Convert UUID to string
            self.stdout.write(self.style.SUCCESS(f"User found: {user.email} (ID: {user_id})"))
        except User.DoesNotExist:
            raise CommandError(f"No user found with email: {user_email}")

        # Define tasks for each day of the week (Sunday to Saturday)
        weekly_tasks = {
            0: [  # Sunday
                {"description": "Arrumar a cama", "points": 20},
                {"description": "Passear com o cachorro", "points": 30},
                {"description": "Ler um livro por 20 minutos", "points": 40},
                {"description": "Ajudar a organizar a casa", "points": 30},
                {"description": "Fazer um desenho ou pintura", "points": 30},
                {"description": "Ajudar a guardar a louça", "points": 50}
            ],
            1: [  # Monday
                {"description": "Arrumar a cama", "points": 20},
                {"description": "Fazer a lição de casa", "points": 40},
                {"description": "Ler um livro por 20 minutos", "points": 40},
                {"description": "Organizar o material escolar", "points": 30},
                {"description": "Ajudar a preparar o lanche", "points": 40},
                {"description": "Guardar os brinquedos", "points": 30}
            ],
            2: [  # Tuesday
                {"description": "Arrumar a cama", "points": 20},
                {"description": "Fazer a lição de casa", "points": 40},
                {"description": "Ler um livro por 20 minutos", "points": 30},
                {"description": "Ajudar a organizar a sala", "points": 40},
                {"description": "Ajudar a cuidar das plantas", "points": 40},
                {"description": "Guardar os brinquedos", "points": 30}
            ],
            3: [  # Wednesday
                {"description": "Arrumar a cama", "points": 20},
                {"description": "Fazer a lição de casa", "points": 50},
                {"description": "Ler um livro por 20 minutos", "points": 30},
                {"description": "Ajudar a separar o lixo reciclável", "points": 50},
                {"description": "Ajudar a organizar os brinquedos", "points": 30},
                {"description": "Fazer um desenho ou pintura", "points": 20}
            ],
            4: [  # Thursday
                {"description": "Arrumar a cama", "points": 20},
                {"description": "Fazer a lição de casa", "points": 40},
                {"description": "Ler um livro por 20 minutos", "points": 30},
                {"description": "Ajudar a limpar o quarto", "points": 50},
                {"description": "Ajudar a preparar o jantar", "points": 40},
                {"description": "Guardar os brinquedos", "points": 20}
            ],
            5: [  # Friday
                {"description": "Arrumar a cama", "points": 20},
                {"description": "Fazer a lição de casa", "points": 40},
                {"description": "Ler um livro por 20 minutos", "points": 30},
                {"description": "Ajudar a limpar a cozinha", "points": 50},
                {"description": "Organizar os materiais escolares", "points": 30},
                {"description": "Fazer um desenho ou pintura", "points": 30}
            ],
            6: [  # Saturday
                {"description": "Arrumar a cama", "points": 20},
                {"description": "Passear com o cachorro", "points": 40},
                {"description": "Ler um livro por 20 minutos", "points": 30},
                {"description": "Ajudar a preparar o almoço", "points": 50},
                {"description": "Ajudar a organizar o quarto", "points": 40},
                {"description": "Fazer um desenho ou pintura", "points": 20}
            ]
        }

        # Date range: December 2024 through December 2025
        start_date = date(2024, 12, 1)
        end_date = date(2025, 12, 31)

        # Get the last pk from the existing DailyMission objects
        last_pk = DailyMission.objects.last().pk if DailyMission.objects.exists() else 0
        pk = last_pk + 1

        # Generate fixture
        fixture = []
        current_date = start_date

        while current_date <= end_date:
            day_of_week = current_date.weekday()  # 0=Monday, 6=Sunday
            daily_tasks = weekly_tasks.get(day_of_week, [])

            for task in daily_tasks:
                fixture.append({
                    "model": "core.dailymission",
                    "pk": pk,
                    "fields": {
                        "description": task["description"],
                        "points": task["points"],
                        "is_completed": False,
                        "target_date": current_date.strftime("%Y-%m-%d"),
                        "fk_user": user_id  # User ID as string
                    }
                })
                pk += 1

            current_date += timedelta(days=1)

        # Determine the path to save the fixture
        fixture_path = os.path.join("src/core/fixtures", "daily_missions.json")

        # Save the fixture to the file
        with open(fixture_path, "w", encoding="utf-8") as f:
            json.dump(fixture, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f"Fixture created with {len(fixture)} entries at {fixture_path}."))

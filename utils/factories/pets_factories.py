from src.condominium.models import Residential
from src.core.models import Color
from src.pets.models.model_animal_species import AnimalSpecies
from src.pets.models.model_pet import Pet
from src.pets.models.model_animal_size import AnimalSize
from src.pets.models.model_animal_breed import AnimalBreed

from utils.factories.condominium_factories import CondominiumFactory


class PetsFactory:
    """
        This class is a container for helper functions that create 'Pets' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Pets' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")

    @staticmethod
    def create_animal_species(description: str = 'Cat') -> AnimalSpecies:
        animal_species, _ = AnimalSpecies.objects.get_or_create(
            description=description)

        return animal_species

    @staticmethod
    def create_animal_breed(description: str = 'Caramel',
                            fk_animal_species: AnimalSpecies | None = None) -> AnimalBreed:

        if not fk_animal_species:
            fk_animal_species = PetsFactory.create_animal_species('Dog')

        animal_bread, _ = AnimalBreed.objects.get_or_create(description=description,
                                                            fk_animal_species=fk_animal_species)
        return animal_bread

    @staticmethod
    def create_animal_size(description: str = 'Small') -> AnimalSize:
        animal_size, _ = AnimalSize.objects.get_or_create(
            description=description)
        return animal_size

    @staticmethod
    def create_pet(name: str = 'Doggo',
                   fk_animal_breed: AnimalBreed | None = None,
                   fk_animal_size: AnimalSize | None = None,
                   fk_animal_color: Color | None = None,
                   fk_residential: Residential = None) -> Pet:

        if not fk_residential:
            fk_residential = CondominiumFactory.create_residential()

        if not fk_animal_breed:
            fk_animal_breed = PetsFactory.create_animal_breed()

        pet = Pet.objects.create(
            name=name,
            fk_animal_breed=fk_animal_breed,
            fk_animal_size=fk_animal_size,
            fk_animal_color=fk_animal_color,
            fk_residential=fk_residential
        )

        return pet

    @staticmethod
    def create_all_pet_data() -> Pet:
        PetsFactory.create_animal_species('Cachorro')
        PetsFactory.create_animal_species('Gato')

        PetsFactory.create_animal_breed(
            'Sem Raça Definida', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Sem Raça Definida', AnimalSpecies.objects.get(description='Gato'))

        PetsFactory.create_animal_breed(
            'Shih Tzu', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Labrador Retriever', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Golden Retriever', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Poodle', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Yorkshire Terrier', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Beagle', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Bulldog Francês', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Dachshund (Salsicha)', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Rottweiler', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Boxer', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Chihuahua', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Pastor Alemão', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Pinscher', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Border Collie', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Cocker Spaniel', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Lhasa Apso', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Dálmata', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Maltês', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Doberman', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Buldogue Inglês', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Pug', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Husky Siberiano', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Shiba Inu', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Basset Hound', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Schnauzer', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Samoieda', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Shar-Pei', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Staffordshire Bull Terrier', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Chow Chow', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Akita Inu', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Pomerânia (Spitz Alemão Anão)', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Bernese Mountain Dog (Boiadeiro Bernês)', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Dogue Alemão', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Pequinês', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Boston Terrier', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Cavalier King Charles Spaniel', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Shetland Sheepdog (Sheltie)', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Dogo Argentino', AnimalSpecies.objects.get(description='Cachorro'))
        PetsFactory.create_animal_breed(
            'Staffordshire Terrier Americano', AnimalSpecies.objects.get(description='Cachorro'))

        PetsFactory.create_animal_breed(
            'Persa', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Siamês', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Maine Coon', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Bengal', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Sphynx', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Ragdoll', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Scottish Fold', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'British Shorthair', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Abissínio', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Burmês', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Exótico', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Himalaio', AnimalSpecies.objects.get(description='Gato'))
        PetsFactory.create_animal_breed(
            'Azul Russo', AnimalSpecies.objects.get(description='Gato'))

from src.condominium.models import Residential
from src.condominium.models import Commercial
from src.core.models import Color
from src.vehicles.models import VehicleModel, Vehicle, VehicleManufacturer

from utils.factories.condominium_factories import CondominiumFactory
from utils.factories.core_factories import CoreFactory


class VehiclesFactory:
    """
        This class is a container for helper functions that create 'Vehicles' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Vehicles' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")

    @staticmethod
    def create_vehicle_manufacturer(description: str = 'Honda') -> VehicleManufacturer:
        vehicle_manufacturer, _ = VehicleManufacturer.objects.get_or_create(
            description=description)
        return vehicle_manufacturer

    @staticmethod
    def create_vehicle_model(
            description: str = 'Civic LXR',
            fk_vehicle_manufacturer: VehicleManufacturer | None = None) -> VehicleModel:

        if not fk_vehicle_manufacturer:
            fk_vehicle_manufacturer = VehiclesFactory.create_vehicle_manufacturer()

        vehicle_model, _ = VehicleModel.objects.get_or_create(description=description,
                                                              fk_vehicle_manufacturer=fk_vehicle_manufacturer)
        return vehicle_model

    @staticmethod
    def create_vehicle(vehicle_plate: str = 'ABC-1234',
                       manufacturing_year: int = 2000,
                       fk_vehicle_model: VehicleModel | None = None,
                       fk_color: Color | None = None,
                       fk_residential: Residential = None) -> Vehicle:

        if not fk_vehicle_model:
            fk_vehicle_model = VehiclesFactory.create_vehicle_model()

        if not fk_color:
            fk_color = CoreFactory.create_color()

        if not fk_residential:
            fk_residential = CondominiumFactory.create_residential()

        return Vehicle.objects.create(
            vehicle_plate=vehicle_plate,
            fk_vehicle_model=fk_vehicle_model,
            fk_color=fk_color,
            manufacturing_year=manufacturing_year,
            fk_residential=fk_residential,
        )

    @staticmethod
    def create_all_vehicles():
        VehiclesFactory.create_vehicle_manufacturer(description='Lifan')
        VehiclesFactory.create_vehicle_manufacturer(description='Kia')
        VehiclesFactory.create_vehicle_manufacturer(description='Ford')
        VehiclesFactory.create_vehicle_manufacturer(description='Fiat')
        VehiclesFactory.create_vehicle_manufacturer(description='Chevrolet')
        VehiclesFactory.create_vehicle_manufacturer(description='Volkswagen')
        VehiclesFactory.create_vehicle_manufacturer(description='Toyota')
        VehiclesFactory.create_vehicle_manufacturer(description='Hyundai')
        VehiclesFactory.create_vehicle_manufacturer(description='Jeep')
        VehiclesFactory.create_vehicle_manufacturer(description='Renault')
        VehiclesFactory.create_vehicle_manufacturer(description='Honda')
        VehiclesFactory.create_vehicle_manufacturer(description='Nissan')
        VehiclesFactory.create_vehicle_manufacturer(description='Citroën')
        VehiclesFactory.create_vehicle_manufacturer(description='Peugeot')
        VehiclesFactory.create_vehicle_manufacturer(description='BMW')
        VehiclesFactory.create_vehicle_manufacturer(description='Caoa Chery')
        VehiclesFactory.create_vehicle_manufacturer(description='Volvo')
        VehiclesFactory.create_vehicle_manufacturer(description='Audi')
        VehiclesFactory.create_vehicle_manufacturer(description='Mitsubishi')
        VehiclesFactory.create_vehicle_manufacturer(description='Land Rover')

        VehiclesFactory.create_vehicle_model(
            description='530', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Lifan'))
        VehiclesFactory.create_vehicle_model(
            description='X60', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Lifan'))
        VehiclesFactory.create_vehicle_model(
            description='X80', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Lifan'))

        VehiclesFactory.create_vehicle_model(
            description='Bongo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Cadenza', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Carnival', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Cerato', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Mohave', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Niro', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Optima', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Picanto', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Rio', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Sorento', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Soul', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Sportage', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Stinger', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))
        VehiclesFactory.create_vehicle_model(
            description='Stonic', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Kia'))

        VehiclesFactory.create_vehicle_model(
            description='A', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Belina', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Bronco Sport', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Corcel', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Corcel II', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Courier', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Crown Victoria', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Del Rey', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Ecosport', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Edge', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Escort', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Explorer', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-1', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-100', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-1000', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-150', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-2000', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-250', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-350', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-4000', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='F-75', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Fiesta', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Focus', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Fusion', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Galaxie', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Jeep', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Ka', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Ka+', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Landau', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Maverick', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Mondeo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Mustang', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Mustang Mach-e', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Pampa', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Ranger', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Rural', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='T', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Taurus', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Territory', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Transit', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Tudor', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Verona', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))
        VehiclesFactory.create_vehicle_model(
            description='Versailles', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Ford'))

        VehiclesFactory.create_vehicle_model(
            description='147', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='500', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='500e', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Argo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Brava', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Bravo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Cronos', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Doblò', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Ducato', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Fastback', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Fiorino', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Freemont', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Grand Siena', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Idea', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Linea', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Marea', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Mobi', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Oggi', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Palio', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Panorama', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Premio', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Pulse', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Punto', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Scudo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Siena', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Stilo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Strada', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Tipo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Toro', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))
        VehiclesFactory.create_vehicle_model(
            description='Uno', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Fiat'))

        VehiclesFactory.create_vehicle_model(
            description='3100', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='A10', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='A20', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Advanced Design', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Agile', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Astra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Bel Air', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Blazer', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Bolt', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Bolt EUV', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Bonanza', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Brasil', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Brasinca', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='C10', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='C14', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Camaro', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Captiva', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Caravan', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Celta', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Chevelle', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Classic', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Cobalt', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Corsa', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Corvette', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Corvette Grand Sport', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Cruze', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='D10', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='D20', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='De Luxe', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Equinox', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Grand Blazer', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='International', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Joy', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Kadett', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Malibu', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Master', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Meriva', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Montana', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Monza', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Omega', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Onix', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Opala', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Prisma', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='S10', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Silverado', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Sonic', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Spin', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='SS', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Suburban', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Tigra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Tracker', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Trailblazer', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Vectra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Veraneio', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))
        VehiclesFactory.create_vehicle_model(
            description='Zafira', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Chevrolet'))

        VehiclesFactory.create_vehicle_model(
            description='1300', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Amarok', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Apollo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Bora', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Brasilia', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Buggy', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Cross Up', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Crossfox', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Eos', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Eurovan', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Fox', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Fusca', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Gol', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Golf', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Jetta', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Karmann-Ghia', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Kombi', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Logus', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='New Beetle', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Nivus', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Parati', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Passat', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Passat Variant', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Polo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Polo Sedan', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Santana', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Saveiro', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Space Cross', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Spacefox', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='T-Cross', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Taos', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Tiguan', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='TL', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Touareg', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Up', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Variant', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Variant II', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Virtus', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))
        VehiclesFactory.create_vehicle_model(
            description='Voyage', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volkswagen'))

        VehiclesFactory.create_vehicle_model(
            description='Bandeirante', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Camry', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Corolla', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Corolla Cross', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Etios', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Etios Cross', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Fielder', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='FJ Cruiser', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='GR Corolla', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Hilux', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Hilux SW4', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Land Cruiser', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Land Cruiser Prado', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Prius', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='RAV4', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Sienna', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Supra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Tundra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Venza', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))
        VehiclesFactory.create_vehicle_model(
            description='Yaris', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Toyota'))

        VehiclesFactory.create_vehicle_model(
            description='Azera', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Coupê', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Creta', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Elantra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Equus', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Genesis', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Grand Santa Fé', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='HB20', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='HB20S', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='HB20X', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='HR', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='I30', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='I30 CW', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Ioniq', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='IX35', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Kona', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Santa Fé', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Sonata', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Terracan', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Tucson', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Veloster', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))
        VehiclesFactory.create_vehicle_model(
            description='Veracruz', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Hyundai'))

        VehiclesFactory.create_vehicle_model(
            description='Cherokee', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))
        VehiclesFactory.create_vehicle_model(
            description='CJ 5', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))
        VehiclesFactory.create_vehicle_model(
            description='Commander', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))
        VehiclesFactory.create_vehicle_model(
            description='Compass', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))
        VehiclesFactory.create_vehicle_model(
            description='Gladiator', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))
        VehiclesFactory.create_vehicle_model(
            description='Grand Cherokee', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))
        VehiclesFactory.create_vehicle_model(
            description='Renegade', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))
        VehiclesFactory.create_vehicle_model(
            description='Wrangler', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Jeep'))

        VehiclesFactory.create_vehicle_model(
            description='Captur', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Clio', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Duster', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Duster Oroch', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Fluence', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Kangoo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Kwid', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Logan', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Megane', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Oroch', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Sandero', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Scénic', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Stepway', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Symbol', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))
        VehiclesFactory.create_vehicle_model(
            description='Zoe', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Renault'))

        VehiclesFactory.create_vehicle_model(
            description='Accord', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))
        VehiclesFactory.create_vehicle_model(
            description='City', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))
        VehiclesFactory.create_vehicle_model(
            description='Civic', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))
        VehiclesFactory.create_vehicle_model(
            description='CR-V', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))
        VehiclesFactory.create_vehicle_model(
            description='Fit', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))
        VehiclesFactory.create_vehicle_model(
            description='HR-V', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))
        VehiclesFactory.create_vehicle_model(
            description='WR-V', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))
        VehiclesFactory.create_vehicle_model(
            description='ZR-V', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Honda'))

        VehiclesFactory.create_vehicle_model(
            description='200SX', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='350Z', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='370Z', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Altima', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Armada', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Frontier', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Grand Livina', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='GT-R', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Kicks', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Leaf', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Livina', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='March', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Pathfinder', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Sentra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Tiida', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Versa', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='X-Trail', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))
        VehiclesFactory.create_vehicle_model(
            description='Xterra', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Nissan'))

        VehiclesFactory.create_vehicle_model(
            description='Aircross', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='Berlingo', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C3', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C3 Aircross', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C3 Picasso', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C3 Sonora', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C4', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C4 Cactus', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C4 Grand Picasso', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C4 Lounge', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C4 Picasso', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C5', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='C8', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='DS3', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='DS4', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='DS5', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='Grand C4', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='Jumper', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='Jumpy', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='Xsara', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))
        VehiclesFactory.create_vehicle_model(
            description='Xsara Picasso', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Citroën'))

        VehiclesFactory.create_vehicle_model(
            description='2008', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='206', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='207', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='208', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='3008', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='307', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='308', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='308CC', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='408', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='5008', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='Boxer', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='Expert', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='Hoggar', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='Partner', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='Partner Rapid', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))
        VehiclesFactory.create_vehicle_model(
            description='RCZ', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Peugeot'))

        VehiclesFactory.create_vehicle_model(
            description='116i', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))
        VehiclesFactory.create_vehicle_model(
            description='118i', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))
        VehiclesFactory.create_vehicle_model(
            description='120i', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))
        VehiclesFactory.create_vehicle_model(
            description='125i', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))
        VehiclesFactory.create_vehicle_model(
            description='130i', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))
        VehiclesFactory.create_vehicle_model(
            description='135i', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))
        VehiclesFactory.create_vehicle_model(
            description='1602', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))
        VehiclesFactory.create_vehicle_model(
            description='218i', fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))

        # Generate create_vehicle_model for all list model
        for model in [
            '220i', '225i', '316i', '318i', '320i', '323i', '325i', '328i', '330Ci', '330e', '330i', '335i', '420i', '428i',
            '430i', '435i', '528i', '530e', '530i', '535i', '540i', '550i', '640i', '645CI', '650i', '740i', '745Le', '750i',
            '750Li', '760Li', '850i', 'i3', 'I4', 'i7', 'i8', 'iX', 'iX1', 'iX3', 'M 135i', 'M 140i', 'M 235i', 'M 240i',
            'M 340i', 'M 440i', 'M 850i', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'Z3',
            'Z4'
        ]:
            VehiclesFactory.create_vehicle_model(
                description=model, fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='BMW'))

        for model in [
            'Arrizo 5', 'Arrizo 6', 'Arrizo 6 PRO', 'Celer', 'Cielo', 'Face', 'iCAR', 'QQ', 'S-18', 'Tiggo', 'Tiggo 2',
            'Tiggo 3X', 'Tiggo 5x', 'Tiggo 5X PRO', 'Tiggo 7', 'Tiggo 7 PRO', 'Tiggo 8', 'Tiggo 8 PRO'
        ]:

            VehiclesFactory.create_vehicle_model(
                description=model, fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Caoa Chery'))

        for model in [
            '444', 'C30', 'C40', 'EX30', 'S60', 'S70', 'S90', 'V40', 'V60', 'XC40', 'XC60', 'XC90'
        ]:
            VehiclesFactory.create_vehicle_model(
                description=model, fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Volvo'))

        for model in [
            'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'E-TRON', 'Q3', 'Q5', 'Q7', 'Q8', 'Q8 E-TRON', 'R8',
            'RS E-TRON GT', 'RS Q3', 'RS Q8', 'RS3', 'RS4', 'RS5', 'RS6', 'RS7', 'S3', 'S4', 'S5', 'SQ5', 'TT', 'TT RS', 'TTS'
        ]:
            VehiclesFactory.create_vehicle_model(
                description=model, fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Audi'))

        for model in [
            '3000 GT', 'Airtrek', 'ASX', 'Eclipse', 'Eclipse Cross', 'L200', 'L200 Outdoor', 'L200 Savana', 'L200 Triton',
            'Lancer', 'Outlander', 'Outlander Sport', 'Pajero', 'Pajero Dakar', 'Pajero Full', 'Pajero Sport', 'Pajero TR4'
        ]:
            VehiclesFactory.create_vehicle_model(
                description=model, fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Mitsubishi'))

        for model in ['Defender', 'Discovery', 'Discovery 3', 'Discovery 4', 'Discovery Sport', 'Freelander', 'Freelander 2',
                      'Range Rover', 'Range Rover Evoque', 'Range Rover Sport', 'Range Rover Velar', 'Range Rover Vogue']:
            VehiclesFactory.create_vehicle_model(
                description=model, fk_vehicle_manufacturer=VehicleManufacturer.objects.get(description='Land Rover'))

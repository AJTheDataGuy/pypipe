"""Components for the pypipe module"""
from math import pi

class Fluid:
    """"""
    def __init__(self,
                 fluid_name:str,
                 density_kg_per_m3:float,
                 viscosity_pa_s:float,
                 flow_rate_m3_per_s:float
                 ) -> None:
        """placeholder"""
        self.fluid_name = fluid_name
        self.density_kg_per_m3 = density_kg_per_m3
        self.viscosity_pa_s = viscosity_pa_s
        self.flow_rate_m3_per_s = flow_rate_m3_per_s

class Pipe:
    """placeholder"""
    def __init__(self,
                 fluid:Fluid,
                 length_m:float,
                 vertical_delta_m:float,
                 inner_diameter_m:float,
                 relative_roughness:float) -> None:
        """placeholder"""
        self.fluid = fluid
        self.length_m = length_m
        self.vertical_delta_m = vertical_delta_m
        self.inner_diameter_m = inner_diameter_m
        self.relative_roughness = relative_roughness

        def calculate_average_pipe_velocity(self):
            """Pipe average velocity is defined as the flowrate of the fluid
            dvided by the cross sectional area of the pipe


            """
            pipe_inner_area_m2 = pi*(self.inner_diameter_m/2)**2
            self.avg_pipe_velocity = self.fluid.flow_rate_m3_per_s

        def calculate_absolute_roughness(self):
            """Pipe absolute roughness is defined as the relative roughness
            divided by it's inner diameter

            Parameters:
            1. Relative roughness bound to self (dimensonless)
            2. Inner diameter bound to self in metres
            """
            self.absolute_roughness = self.relative_roughness / self.inner_diameter_m

        def calculate_reynolds_number(self):
            self.reynolds_number = (self.fluid.density_kg_per_m3 * self.avg_pipe_velocity_m_per_s * self.inner_diameter_m) / self.fluid.viscosity_pa_s

        def calculate_friction_factor(self):
            pass

        def calculate_if_turbulent_or_laminar(self):
            """Calculates whether the flow in the pipe is
            turbulent or laminar
            
            Flows in a pipe are turbulent for Reynolds numbers over 2000
            and laminar if under 2000

            Parameters:
            1. The Reynolds number (dimensionless) bound to self

            Returns:
            1. Turbulence type bound to self
            """
            if self.reynolds_number > 2000:
                self.turbulence_type = "TURBULENT"
            else:
                self.turbulence_type = "LAMINAR"

        def calculate_pressure_loss(self):
            """placeholder"""
            pass

class Tank:
    """Class to represent a storage tank
    For example, a storage tank of crude petroleum
    """
    def __init__(self,
                 fluid:Fluid,
                 fluid_height_m:float,
                 ) -> None:
        """placeholder"""
        self.fluid = fluid
        self.fluid_height_m = fluid_height_m

    def calculate_fluid_head(self):
        """Fluid head / pressure in a tank is defined as
        fluid density * gravity * height of the fluid

        Parameters:
        1. Fluid density bound to self in units of kg / m^3
        2. Fluid height bound to self in units of meters

        Returns:
        1. Fluid head bound to self in units of [TO BE FILLED IN]
        """
        gravity_m_per_s2 = 9.8
        self.fluid_head = self.fluid.density_kg_per_m3 * gravity_m_per_s2 * self.fluid_height_m
        

class PressureNodeAtStart:
    """Placeholder for an initial pressure node"""
    def __init__(self,pressure_kpa:float) -> None:
        """placeholder"""
        self.pressure_kpa = pressure_kpa

class Valve:
    """Placeholder for a valve class which reduces pressure"""
    def __init__(self) -> None:
        """placeholder"""
        return NotImplementedError

class Pump:
    """Placeholder for a pump class which increases pressure"""
    def __init__(self) -> None:
        """placeholder"""
        return NotImplementedError
    
class Bend:
    """Placeholder for a bends class which redues pressure"""
    def __init__(self) -> None:
        """placeholder"""
        return NotImplementedError

class TJunction:
    """Placeholder for a T Junction class"""
    def __init__(self) -> None:
        """placeholder"""
        return NotImplementedError



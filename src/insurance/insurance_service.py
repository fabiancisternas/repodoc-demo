# Servicio de Seguros — BICE Seguros Demo
# Gestiona seguros personales y asociados a productos

class InsuranceService:
    """
    Gestiona todos los productos de seguros BICE para persona natural.
    Incluye seguros automotriz, vida, hogar, SOAP, viaje y desgravamen.
    """

    def get_active_policies(self, client_id: str):
        """
        Retorna todas las pólizas activas del cliente.
        Incluye: tipo, cobertura, prima mensual, fecha vencimiento, estado.
        """
        pass

    def quote_auto_insurance(self, client_id: str, vehicle_data: dict):
        """
        Genera cotización de seguro automotriz.
        Incluye: cobertura básica, todo riesgo, asistencia 24/7, auto de reemplazo.
        Precio varía según: año vehículo, marca, uso, historial del conductor.
        """
        pass

    def get_claims_history(self, client_id: str):
        """
        Retorna historial de siniestros del cliente.
        Incluye: fecha, tipo, estado, monto liquidado, tiempo de resolución.
        Usado para calcular prima de renovación.
        """
        pass

    def renew_soap(self, client_id: str, vehicle_id: str):
        """
        Renueva el SOAP (Seguro Obligatorio Accidentes Personales).
        Proceso 100% digital, sin papeles.
        Envía certificado por email al completar el pago.
        """
        pass

    def subscribe_life_insurance(self, client_id: str, coverage: float):
        """
        Suscribe al cliente a seguro de vida BICE.
        Coverage: monto asegurado en pesos.
        Prima calculada según: edad, cobertura, historial médico declarado.
        """
        pass

    def get_insurance_recommendations(self, client_id: str):
        """
        Identifica seguros no contratados relevantes para el cliente.
        Lógica: cliente con hipotecario sin seguro hogar = recomendación prioritaria.
        Cliente con vehículo registrado sin SOAP = alerta regulatoria.
        """
        pass

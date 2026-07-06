# Servicio de Inversiones — BICE Inversiones Demo
# Gestiona fondos mutuos, APV, acciones y depósitos

class InvestmentService:
    """
    Gestiona todos los productos de inversión BICE.
    Incluye fondos mutuos, APV, acciones, renta fija y DAP.
    """

    def get_portfolio(self, client_id: str):
        """
        Retorna el portafolio completo de inversiones del cliente.
        Incluye: productos activos, montos, rentabilidad YTD, evolución 12 meses.
        """
        pass

    def get_mutual_funds(self, client_id: str):
        """
        Retorna fondos mutuos activos del cliente.
        Incluye: fondo, monto invertido, rentabilidad, perfil de riesgo.
        Fondos disponibles: conservador, moderado, agresivo, money market.
        """
        pass

    def subscribe_apv(self, client_id: str, amount: float, regime: str):
        """
        Suscribe al cliente a APV (Ahorro Previsional Voluntario).
        Regime: 'A' (rebaja impuestos) o 'B' (beneficio al rescatar).
        Calcula beneficio tributario estimado según ingresos del cliente.
        """
        pass

    def buy_stocks(self, client_id: str, ticker: str, amount: float):
        """
        Ejecuta compra de acciones en bolsa local.
        Ticker: símbolo bursátil (ej: FALABELLA, BICE, COPEC).
        Requiere perfil de inversión aprobado.
        """
        pass

    def create_time_deposit(self, client_id: str, amount: float, days: int):
        """
        Crea un depósito a plazo fijo.
        Días disponibles: 30, 60, 90, 180, 360.
        Retorna tasa ofrecida y monto estimado al vencimiento.
        """
        pass

    def get_investment_recommendations(self, client_id: str):
        """
        Genera recomendaciones de inversión personalizadas.
        Basado en: perfil de riesgo, edad, ingresos, productos actuales.
        Identifica productos no contratados con mayor potencial para el cliente.
        """
        pass

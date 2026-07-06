# Servicio de Tarjetas — Banco BICE Demo
# Gestiona tarjetas de crédito y débito Visa

class CardService:
    """
    Gestiona operaciones de tarjetas de crédito y débito BICE.
    Soporta Visa Gold, Platinum, Signature e Infinite.
    """

    def get_card_balance(self, card_id: str):
        """
        Retorna saldo disponible y utilizado de tarjeta de crédito.
        Incluye cupo total, cupo disponible y monto mínimo a pagar.
        """
        pass

    def get_transactions(self, card_id: str, months: int = 3):
        """
        Retorna transacciones de los últimos N meses.
        Incluye: comercio, monto, cuotas, categoría, dólares BICE ganados.
        """
        pass

    def block_card(self, card_id: str, reason: str):
        """
        Bloquea temporalmente una tarjeta por seguridad o control.
        Razones válidas: perdida, robo, control_gasto, viaje.
        Notifica al cliente por email y push notification.
        """
        pass

    def set_pat(self, card_id: str, service: str, amount: float):
        """
        Inscribe un PAT (Pago Automático con Tarjeta).
        Asocia un servicio recurrente a la tarjeta de crédito.
        Acumula Dólares BICE por cada pago automático realizado.
        """
        pass

    def get_dolares_bice(self, client_id: str):
        """
        Retorna el saldo de Dólares BICE acumulados del cliente.
        Incluye historial de acumulación y canjes realizados.
        1 Dólar BICE = 1 USD en canjes de viajes y retail.
        """
        pass

    def enable_apple_google_pay(self, card_id: str, platform: str):
        """
        Activa Apple Pay o Google Pay para una tarjeta.
        Platform: 'apple' o 'google'.
        Disponible para tarjetas débito y crédito BICE.
        """
        pass

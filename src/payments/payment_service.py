
# Servicio de Pagos — Banco BICE Demo
# Gestiona todos los canales de pago digital

class PaymentService:
    """
    Gestiona los botones de pago y automatización de pagos BICE.
    Incluye PAC, PAT, botones de pago y Previred.
    """

    def pay_service(self, client_id: str, service: str, amount: float):
        """
        Pago de servicios básicos via Botón de Pago BICE.
        Servicios: luz, agua, gas, telefonía, internet, TV cable.
        Débito inmediato desde cuenta corriente o tarjeta.
        Historial disponible por 24 meses.
        """
        pass

    def pay_previred(self, client_id: str, period: str, amount: float):
        """
        Pago de cotizaciones previsionales via Previred.
        Disponible para trabajadores independientes.
        Incluye: AFP, Isapre, SIS, seguro cesantía.
        Genera comprobante oficial descargable.
        """
        pass

    def pay_sii(self, client_id: str, declaration_type: str, amount: float):
        """
        Pago de impuestos al SII y Tesorería General de la República.
        Tipos: F22, F29, contribuciones, otros.
        Integrado directamente con plataforma SII.
        """
        pass

    def setup_pac(self, client_id: str, service: str, account_id: str):
        """
        Configura PAC (Pago Automático con Cargo a Cuenta Corriente).
        El servicio cobra automáticamente cada mes.
        Cliente recibe notificación 3 días antes del cargo.
        """
        pass

    def get_payment_history(self, client_id: str, months: int = 12):
        """
        Retorna historial completo de pagos del cliente.
        Incluye: PAC, PAT, botones de pago, Previred, SII.
        Agrupado por categoría y canal utilizado.
        """
        pass

    def schedule_payment(self, client_id: str, service: str, 
                        amount: float, date: str):
        """
        Programa un pago futuro para una fecha específica.
        El cliente recibe recordatorio 24h antes.
        Cancela automáticamente si no hay fondos suficientes y notifica.
        """
        pass

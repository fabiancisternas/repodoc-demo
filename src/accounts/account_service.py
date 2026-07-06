# Servicio de Cuentas — Banco BICE Demo
# Gestiona operaciones de cuentas corrientes y vistas

class AccountService:
    """
    Gestiona todas las operaciones relacionadas con cuentas bancarias.
    Soporta cuenta corriente en pesos, dólares y Cuenta GO BICE.
    """

    def get_balance(self, account_id: str, currency: str = "CLP"):
        """
        Retorna el saldo disponible de una cuenta.
        Soporta CLP, USD y EUR.
        """
        pass

    def get_movements(self, account_id: str, months: int = 12):
        """
        Retorna los movimientos de los últimos N meses.
        Por defecto retorna 12 meses de historial.
        Incluye: fecha, monto, descripción, categoría, canal.
        """
        pass

    def transfer(self, from_account: str, to_account: str, amount: float):
        """
        Realiza transferencia entre cuentas propias o a terceros.
        Aplica límites diarios según perfil del cliente.
        Registra canal utilizado (app, web, sucursal).
        """
        pass

    def set_overdraft_limit(self, account_id: str, limit: float):
        """
        Configura el límite de la línea de sobregiro.
        Solo disponible para clientes con cuenta corriente activa.
        """
        pass

    def get_account_summary(self, client_id: str):
        """
        Retorna resumen consolidado de todas las cuentas del cliente.
        Incluye: saldo total, movimientos del mes, alertas activas.
        """
        pass

from fpdf import FPDF
from controllers.controladorPedidos import ControladorPedidos

ControladorArticulos2 = ControladorPedidos()

class GenerarPDFPedidos(FPDF):
    
    def header(self):
        self.set_font("Times", "BU", 14)
        self.cell(0, 10, "Reporte de Pedidos", 0, 1, "C")
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, "Página %s" % self.page_no(), 0, 0, "C")
    
    def chapter_body(self):
        self.set_font("Arial", "", 10)
        self.set_fill_color(255, 250, 250)
        
    
        headers = ["ID", "Solicitante", "Departamento", "Estado"] 
        
        col_widths = [20,55,55,55]
        
        effective_page_width = self.w - 2 * self.l_margin
        table_width = sum(col_widths)
        x_position = abs(self.l_margin + (effective_page_width - table_width) / 2)
        
        self.set_xy(x_position, self.get_y())
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, 1, 0, "C", 1)
        self.ln()
        
    
        listaPedidos = ControladorArticulos2.listaPedidos2xd()
        
        for pedido in listaPedidos:
            self.set_xy(x_position, self.get_y())
            for i, cell in enumerate(pedido):
                self.cell(col_widths[i], 10, str(cell), 1, 0, "C")
            self.ln()

from PySimpleGUI import PySimpleGUI as sg
from PIL import Image, ImageDraw, ImageFont

# Transferir os dados da planilha para a imagem do certificado
font_nome = ImageFont.truetype('./tahomabd.ttf', 50)
font_geral = ImageFont.truetype('./tahoma.ttf', 50)
font_data = ImageFont.truetype('./tahoma.ttf', 50)

image = Image.open('./certificado_padrao.png')
desenhar = ImageDraw.Draw(image)

# Layout

sg.theme('Reddit')

layout = [
    [sg.Text('Nome do Curso'), sg.Input(key='nome_curso')],
    [sg.Text('Nome do Participante'), sg.Input(key='nome_participante')],
    [sg.Text('Tipo de Participação'), sg.Input(key='tipo_participacao')],
    [sg.Text('Data de início'), sg.Input(key='data_inicio')],
    [sg.Text('Data final'), sg.Input(key='data_final')],
    [sg.Text('Carga horária'), sg.Input(key='carga_horaria')],
    [sg.Text('Data de emissão'), sg.Input(key='data_emissao')],
    [sg.Text('Laboratório'), sg.Input(key='laboratorio')],
    [sg.Button('Gerar'), sg.Button('Novo Certificado')],
]

# Janela

janela = sg.Window('Gerar Certificado', layout, size=(270,300))

# Remove 

# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Gerar':
        nome_curso = valores['nome_curso']
        nome_participante = valores['nome_participante']
        tipo_participacao = valores['tipo_participacao']
        data_inicio = valores['data_inicio']
        data_final = valores['data_final']
        carga_horaria = valores['carga_horaria']
        data_emissao = valores['data_emissao']
        laboratorio = valores['laboratorio']
        
        desenhar.text((510,330), nome_participante, fill='black', font=font_nome)
        desenhar.text((660,390), str(laboratorio), fill='black', font=font_geral)
        desenhar.text((510,458), nome_curso, fill='black', font=font_geral)
        desenhar.text((900,520), tipo_participacao, fill='black', font=font_geral)
        desenhar.text((730,585), str(carga_horaria) + ' horas', fill='black', font=font_geral)
        desenhar.text((320,970), str(data_inicio), fill='blue', font=font_data)
        desenhar.text((320,1150), str(data_final), fill='blue', font=font_data)
        desenhar.text((1480,1040), str(data_emissao), fill='blue', font=font_data)

        image.save(f'./certificados/{nome_participante} certificado.png')

    if eventos == 'Novo Certificado':
        janela.FindElement('nome_curso').Update('')
        janela.FindElement('nome_participante').Update('')
        janela.FindElement('tipo_participacao').Update('')
        janela.FindElement('data_inicio').Update('')
        janela.FindElement('data_final').Update('')
        janela.FindElement('carga_horaria').Update('')
        janela.FindElement('data_emissao').Update('')
        janela.FindElement('laboratorio').Update('')
    
    
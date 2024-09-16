import utils
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

pandas2ri.activate()

robjects.r['source']('api-clima.r')

clima = robjects.r['clima']

plantacoes = {
  'banana': {
    'cidade': '',
    'formato_terreno': 'retângulo', 
    'largura': 0, 
    'comprimento': 0,
    'area': lambda: utils.area_retangulo(plantacoes['banana']['largura'], plantacoes['banana']['comprimento']),
    'insumos': {
      'mudas': lambda: ((plantacoes['banana']['comprimento'] / 3) + 1) * ((plantacoes['banana']['largura'] / 4) + 1),
      'adubacao': [
        {
          'adubo': 'Sulfato de amônio',
          'gramas': lambda: 1200 * plantacoes['banana']['insumos']['mudas']()
        },
        {
          'adubo': 'Superfosfato simples',
          'gramas': lambda: 400 * plantacoes['banana']['insumos']['mudas']()
        },
        {
          'adubo': 'Cloreto de Potássio',
          'gramas': lambda: 1200 * plantacoes['banana']['insumos']['mudas']()
        }
      ]
    }
  }, 
  
  'tomate': {
    'cidade': '',
    'formato_terreno': 'círculo', 
    'raio': 0,
    'area': lambda: utils.area_circulo(plantacoes['tomate']['raio']),
    'insumos': {
      'mudas': lambda: plantacoes['tomate']['area']() / 0.5,
      'adubacao': [
        {
          'adubo': 'Esterco bovino',
          'gramas': lambda: 1500 * plantacoes['tomate']['insumos']['mudas']()
        }
      ]
    }
  }
}

def menu():
  print('\nMenu:')
  print('[1] Inserir dados')
  print('[2] Exibir dados')
  print('[3] Atualizar dados')
  print('[4] Deletar dados')
  print('[5] Sair do programa')
  return input("Escolha uma opção: ")

def inserir():
  plantacao = input('Digite o tipo de plantação (banana/tomate): ').strip().lower()
  
  if plantacao == 'banana':
    plantacoes['banana']['largura'] = float(input('Digite a largura (m) do terreno: '))
    plantacoes['banana']['comprimento'] = float(input('Digite o comprimento (m) do terreno: '))
    
  elif plantacao == 'tomate':
    plantacoes['tomate']['raio'] = float(input('Digite o raio (m) do terreno: '))
    
  else:
    print('Não encontrado')

  plantacoes[plantacao]['cidade'] = input('Digite sua cidade: ')
  
def exibir():
  plantacao = input('Digite o tipo de plantação (banana/tomate): ').strip().lower()

  if plantacoes[plantacao]['cidade'] != '':
  
    print(f'\n----- Plantação de {plantacao.capitalize()} -----')
      
    print(f'Área do terreno: {plantacoes[plantacao]['area']():.2f}m²')

    print('\n> Clima:')

    df_clima = clima(plantacoes[plantacao]['cidade'])

    clima_info = pandas2ri.rpy2py(df_clima)

    for row in clima_info.itertuples():
      print(f'{row.item}{row.valor}{row.unid_medida}')
    
    print('\n> Insumos necessários:')

    print(f'- {plantacoes[plantacao]['insumos']['mudas']():.0f} mudas de {plantacao}')

    for insumo in plantacoes[plantacao]['insumos']['adubacao']:
      print(f'- {utils.unidade_adubo(insumo['gramas']())} de {insumo['adubo']}')

  else:
    print('Não há dados para serem exibidos.')
    
def atualizar():
  plantacao = input('Digite o tipo de plantação (banana/tomate): ').strip().lower()
  
  if plantacao == 'banana':
    plantacoes['banana']['largura'] = float(input('Digite a nova largura (m) do terreno: '))
    plantacoes['banana']['comprimento'] = float(input('Digite o novo comprimento (m) do terreno: '))
    plantacoes['banana']['cidade'] = input('Digite sua cidade: ')
    
  elif plantacao == 'tomate':
    plantacoes['tomate']['raio'] = float(input('Digite o novo raio (m) do terreno: '))
    plantacoes['tomate']['cidade'] = input('Digite sua cidade: ')
    
  else:
    print('Não encontrado')
  
def deletar():
  plantacao = input('Digite o tipo de plantação (banana/tomate): ').strip().lower()
  
  if plantacao == 'banana':
    plantacoes['banana']['largura'] = 0
    plantacoes['banana']['comprimento'] = 0
    plantacoes['banana']['cidade'] = ''
    
  elif plantacao == 'tomate':
    plantacoes['tomate']['raio'] = 0
    plantacoes['banana']['cidade'] = ''
    
  else:
    print('Não encontrado')

  print('Dados deletados.')
    
# Loop principal
while True:
  opc = menu()
  if opc == '1':
    inserir()
  elif opc == '2':
    exibir()
  elif opc == '3':
    atualizar()
  elif opc == '4':
    deletar()
  elif opc == '5':
    print("Saindo do programa...\n")
    break
  else:
    print("Opção inválida, tente novamente.")
    
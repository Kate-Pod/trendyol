import pathlib
from dash import Dash, html, dcc, dash_table, Input, Output, callback, ctx
# import dash_auth
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
# from CategoryChoice import choose_category, get_subcategory
# from config import VALID_USERNAME_PASSWORD_PAIRS
import warnings
warnings.filterwarnings("ignore")

standard_BS = dbc.themes.BOOTSTRAP

colors = ['#C997FD',
          '#f5f2e8',
          '#f8f3e3',
          '#ffffff',
          ]
app = Dash(__name__, external_stylesheets=[standard_BS])
# Declare server for Heroku deployment. Needed for Procfile.
server = app.server
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
df = pd.read_excel(DATA_PATH.joinpath('grouped_first.xlsx'))
main = pd.read_csv(DATA_PATH.joinpath('demo_result.csv.gz'))

# df = pd.read_excel('grouped_first.xlsx')
# main = pd.read_csv('demo_result.csv.gz')

main = main[main['unique_id'].isin(['114729009_199013_61_c0d737e52d04f93a5279822cd457d547',
       '6026206_166423_613344_19a7d9c4e02d46f2b4c2af7f1c9e208a',
       '239841996_250511_61_a5b84151ab320194c67f6e0366f810d8',
       '86445518_252403_61_735e29e06b381ce51cfd93ffa674c4f5',
       '115457179_270844_61_1ed7f5e29a7f46bffd276920b59b3cdb',
       '52559960_231895_606554_81990b76bac503b740ef5cda5e9a2a2d',
       '44620237_213499_61_e6adb2cffcadec918c1c3f8fb5e667d1',
       '3019731_682013_61_2c25b2c8cd6a41d3a0fc6c3a40682e5e',
       '338641845_664854_61_23cdcbfe08fb956f02251f0fde61b3f8',
       '341885425_675672_61_72bf08d693c791bd45393b66e50b48fe',
                                    '346309898_662813_61_d534ed38827b111d680cdda8cf9b3ad9',
                                    '346902487_680526_614353_e42c806c6ca980afff8f7ee2c9c4d27d',
                                    '230264709_680093_61_a6c071661889a56fcc9b24c72b5bf529',
                                    '338749711_657326_61_a4091bb623dccd57b3e97b059414cefe',
                                    '311530209_613550_616776_142a544388504909bdc74a19515af924',
                                    '350420006_653684_61_6ac94d25ce602f359842936e2112fa0c',
                                    '82611235_610999_616776_2058b60b1def4ae01fc9adbe78f9d22a',
                                    '2797982_603348_61_52b0fa8b55aa9219922ef41f6c88c30c',
                                    '3886578_655533_61_c2333e625a155f4b32332327608c4372',
                                    '353976015_685557_61_5deecc8f84359cba3a31d2c8e9f9c113',
                                    '6877586_115689_61_a758b77a20e67e12868060202fe9b5cb',
                                    '34268771_113000_61_130cebd9fb714bee2623b4c4912cef6a',
                                    '225361108_530085_606554_8bbab17ec1e0d75b18d2a7115ad8abc4',
                                    '267670652_548487_61_d3332d78b4ed6a074cf4c960d67f402f',
                                    '318246375_553540_61_ad2700beda851ce4397b7b979b2e5fe8',
                                    '168008375_337620_61_097a7acee4e3a6743a0363975a66a88d',
                                    '86165899_324854_614353_ef5115b2649df2a0a7770335d79e30e3',
                                    '6236162_341233_61_2c0a051fffbe7e33f9af2a3cc791c531',
                                    '88558971_345103_61_6ffe08bf4e11b0169b389cda4c2cf27d',
                                    '4802396_287218_61_c2619838cc3afadcda1648344bef5e75',
                                    '262113419_298820_61_7c378c3e453bc1739d0fa0180e469ab0',
                                    '4491729_447242_61_041f05dab340236543f72f2c9109d1f4',
                                    '119028267_414543_61_703afea1bf1b2b48a3fe3598a0c5111c',
                                    '46036528_422393_61_5e941b654b4f4870da6238af054aeec5',
                                    '94038870_355713_61_7d353a5940c0789e4cf2a877010bb07c',
                                    '14631109_424168_61_7b494379d0abaf6923d000072663de1c',
                                    '6952403_155548_61_aad22bf79d4bba467e9eb508da13028a',
                                    '39633570_155996_613832_f254110bc8271e497946208d4f6f8752',
                                    '108911983_153086_61_3f3cfdaad48de01e8c271dbd853f5f5e',
                                    '39146657_149767_606554_50a78930453f2531932703c8968fd081',
                                    '142747916_161616_613832_7cc0e78e059e4b044320e1f372a3de81',
                                    '42224142_172332_606554_b56c41b52517ddc38a58346b730f25c8',
                                    '2584634_141890_61_70862b8803865184966d0150ccce8232',
                                    '2797707_140985_61_5b004b7a5cb096a894ac9cb565a4d0b7',
                                    '204602357_139035_606554_a32d63ae34592781fc24fbfa63c4557b',
                                    '137482002_146612_61_0581dc6eac8204915bfa13f19d8d9f6f',
                                    '267560183_220868_61_deb2f78b1d6fe4811cd73f46524e60e0',
                                    '51518801_223993_613344_742af19ae7fb99d169d0313a232ca97f',
                                    '69935181_197874_614353_764d11d553c6a6ad3cf034728cade334',
                                    '39632014_184447_61_d565f5ba009585338459272677847f82'
                                    ])]
# main = main[main.load_date.isin(['2022-11-20', '2022-11-21', '2022-11-22'])].sample(100000)


# main = main.rename(columns={'QuantityDecrease': 'Продажи'})
main.loc[main['Продажи']>0, 'positive_availableQuantity'] = 1  # availableQuantity нет на исторические даты
main['positive_availableQuantity'] = main['positive_availableQuantity'].fillna(0)
LAST_DAY = pd.to_datetime(main['load_date']).max().strftime('%Y-%m-%d')

logo = html.Img(src=app.get_asset_url('logo.png'), style={'width': "58px", 'height': "55px",'color': 'white'},
                className='inline-image', alt='MarketplaceInfo')
header = html.H3("Ürüntrend", style={'text-transform': "uppercase"})

logo_and_header = dbc.Form(
    dbc.Row(
        [html.Div(
   [html.Div(logo, style={'display': 'inline-block'}),
   html.Div(header, style={'display': 'inline-block'})]
)], className='form-row', ))

app.layout = html.Div(
    [dbc.Container(
        dbc.Row(
             [dbc.Col(
                html.Div(
                    logo_and_header,), ),
             ],
             style={'max-height': '128px', 'color': 'white',}
                ),
        className='d-flex justify-content-center',
        style={'max-width': '100%', 'background-color': colors[0]},
    ),
    dbc.Container(
        html.Div(
              [ html.Br(),html.H5("Выбор ниши", style={'text-align':'center', 'text-transform': 'uppercase'}),
                html.Hr(), # разделительная линия
              ])
    ),
    dbc.Container([
        dbc.Label('Click a cell in the table:'),
        dash_table.DataTable(
            df.to_dict('records'), [{"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns], id='tbl',
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="lightgrey", fontWeight='bold'),
            style_data=dict(backgroundColor="white"), filter_action='native',
            sort_action='native',
            page_size= 15
            # row_selectable='multi'

        ),
         dbc.Alert(id='tbl_out'),
    ]),
    dbc.Container(
        html.Div(
              [ html.Br(),html.H5("Категории", style={'text-align':'center', 'text-transform': 'uppercase'}),
                html.Hr(), # разделительная линия
              ])
    ),
    dbc.Container([
        html.H3('Бизнес-юнит'),
        dcc.Dropdown(main['businessUnit'].unique(), main['businessUnit'].unique()[0],
                     id='bu', placeholder="Выберите Бизнес-юнит",
                     style={'width': '500px'}),

    ]),
    dbc.Container([
            html.H3('Категория 1'),
            dcc.Dropdown(main['Category_1'].unique(), main['Category_1'].unique()[0],
                         id='category_1', placeholder="Выберите категорию",
                         style={'width': '500px'}),

        ]),
    dbc.Container([
        html.H3('Категория 2'),
        dcc.Dropdown(main['Category_2'].unique(), main['Category_2'].unique()[0],
                     id='category_2', placeholder="Выберите категорию",
                     style={'width': '500px'}),
        html.Br(),

    ]),

    dbc.Container([
            dash_table.DataTable(
                main.to_dict('records'),
                [{"name": i, "id": i, "deletable": True, "selectable": True} for i in main.columns],
                id='tbl2',
                style_cell=dict(textAlign='left', textOverflow='ellipsis', overflow='hidden',
                                ),
                style_cell_conditional=[
                    {'if': {'column_id': 'unique_id'},
                        'minWidth': '105px', 'width': '105px', 'maxWidth': '105px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Фото'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Ссылка'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Название'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Category_1'},
                     'minWidth': '120px', 'width': '120px', 'maxWidth': '120px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Category_2'},
                     'minWidth': '120px', 'width': '120px', 'maxWidth': '120px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Category_3'},
                     'minWidth': '120px', 'width': '120px', 'maxWidth': '120px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'categoryName'},
                     'minWidth': '120px', 'width': '120px', 'maxWidth': '120px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Бренд'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Наличие'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Отзывы'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Средний рейтинг'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Цена'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Цена со скидкой'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Был в наличии'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Продаж'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    {'if': {'column_id': 'Выручка'},
                     'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                     'textOverflow': 'ellipsis', 'overflow': 'hidden'},
                    ],
                style_header=dict(backgroundColor="lightgrey", fontWeight='bold'),
                style_data=dict(backgroundColor="white"), filter_action='native',
                sort_action='native',
                page_size=15,
                fill_width=False
            )]),

    dbc.Container([
        html.H3('Выберите предмет анализа'),
        dcc.Dropdown(['Category_3', 'Бренд', 'Тренд', 'Ценовая сегментация'], 'Category_3', id='selector_drop', # 'Продавцы'
                     placeholder="Выберите категорию",
                     style={'width': '500px'}),
        html.Br(),

    ]),

    dbc.Container([html.H4('Доп'), dcc.Dropdown(['Продаж', 'Выручка', 'Товаров', 'Товаров с продажами', 'Число брендов',
                                 'Брендов с продажами', 'Число селлеров', 'Селлеров с продажами', 'Выручка на товар'
                                 ], id='graph_selector',
                     placeholder="...", multi=True,
                     style={'width': '500px'}),
        html.Br(),
]),
    dbc.Container([
        dcc.Graph(
                id='pie_graph'
            )
    ]),

    dbc.Container([
    html.Div(
            [dcc.Input(id='input_min', type='number', value=0),
            dcc.RangeSlider(id='range_slider', min=0, max=30,),
            dcc.Input(id='input_max', type='number', value=30),
            html.Div([], style={"grid-template-columns": "30%"}),
            html.Div([html.H6('Сегментов'), dcc.Input(id="input_segm", type="number", value=15, min=2, max=50,)],
                     style={"display": "grid", "grid-template-columns": "30% 20%"})
             ],
            style={"display": "grid", "grid-template-columns": "10% 50% 10% 2% 28%"}
          )
    ]),

    dbc.Container([dash_table.DataTable(
            main.to_dict('records'),
            [{"name": i, "id": i, "deletable": True, "selectable": True} for i in main.columns],
            id='subcat_table',
            style_cell=dict(textAlign='left', textOverflow='ellipsis', overflow='hidden',
                            ),
            style_header=dict(backgroundColor="lightgrey", fontWeight='bold'),
            style_data=dict(backgroundColor="white"), filter_action='native',
            sort_action='native',
            page_size=15,
            fill_width=False
        )]),

])

@app.callback(
    Output('tbl_out', 'children'),
    Input('tbl', 'active_cell'))
def update_table1(active_cell):
    return str(active_cell) if active_cell else "Click the table"

# a callback from the BU dropdown to the Category_1 Dropdown
@app.callback(
    Output('category_1', 'options'),
    Input('bu', 'value'))
def update_cat1(bu):
    cat1_val = main[['businessUnit', 'Category_1']].drop_duplicates()
    relevant_cat1_options = cat1_val[cat1_val['businessUnit'] == bu]['Category_1'].values.tolist()
    relevant_cat1_options_list = [{'label': x, 'value': x} for x in relevant_cat1_options]
    return relevant_cat1_options_list


# a callback from the Category_1 dropdown to the Category_2 Dropdown
@app.callback(
    Output('category_2', 'options'),
    Input('category_1', 'value'))
def update_cat2(category_1):
    cat2_val = main[['Category_1', 'Category_2']].drop_duplicates()
    relevant_cat2_options = cat2_val[cat2_val['Category_1'] == category_1]['Category_2'].values.tolist()
    relevant_cat2_options_list = [{'label': x, 'value': x} for x in relevant_cat2_options]
    return relevant_cat2_options_list


# update Category data
@app.callback(
    Output('tbl2', 'data'), Output('tbl2', 'columns'),
    Input('category_2', 'value'))
def update_df(category_2):
    new_main = main[(main['Category_2'] == category_2)][
        ['unique_id', 'images', 'url', 'name', 'Category_1', 'Category_2', 'Category_3',
         'categoryName', 'brand_name']].drop_duplicates()
    last_date_info = \
        main[(main['Category_2'] == category_2) & (main['load_date'] == LAST_DAY)].groupby(
            ['unique_id'], as_index=False)['positive_availableQuantity', 'RewiewsCount','averageRating', 'availableQuantity',
                                           'sellingPrice', 'discountedPrice'].mean()

    sales_product = main[(main['Category_2'] == category_2)].groupby(
            ['unique_id'], as_index=False)['Продажи', 'Выручка'].sum()

    new_main = new_main.merge(
        sales_product, on='unique_id', how='left').merge(last_date_info, on='unique_id', how='left')

    new_main.columns = ['unique_id', 'Фото', 'Ссылка', 'Название', 'Category_1', 'Category_2',
                        'Category_3', 'categoryName', 'Бренд',
                        'Продаж', 'Выручка', 'Наличие', 'Отзывы', 'Средний рейтинг', 'Был в наличии', 'Цена',
                        'Цена со скидкой']
    new_main[new_main.columns] = new_main[new_main.columns].fillna(0)
    new_main['Выручка'] = round(new_main['Выручка'], 0).astype(int)
    new_main['Отзывы'] = round(new_main['Отзывы'], 0).astype(int)
    new_main['Наличие'] = new_main['Наличие'].fillna(0)
    new_main['Наличие'] = round((new_main['Наличие']), 0).astype(int)
    new_main['Был в наличии'] = round((new_main['Был в наличии']), 0).astype(int)
    new_main['Средний рейтинг'] = round(new_main['Средний рейтинг'], 2)
    # !!!!!!!
    new_main = new_main.head(500)
    return new_main.to_dict('records'), [{"name": i, "id": i, "deletable": True, "selectable": True} for i in new_main.columns]


# update Category for each dropdown select
@app.callback(
    Output('subcat_table', 'data'), Output('subcat_table', 'columns'),
    Input('selector_drop', 'value'),
    Input('category_1', 'value'),
    Input('category_2', 'value'),
    Input('input_segm', 'value'),
    [Input('tbl2', 'data'),
     Input('tbl2', 'columns')])
def choose_analysisarea(selector_drop, category_1, category_2, input_segm, rows, columns):
    df_area = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    if selector_drop == 'Category_3':
        subcat_analysis = df_area.groupby(['Category_2', 'Category_3'], as_index=False).agg(
            {'Средний рейтинг': 'mean',
             'Отзывы': 'mean',
             'Продаж': 'sum',
             'Выручка': 'sum',
             'Цена': 'mean',
             'unique_id': 'nunique'
             }).rename(columns={'unique_id': 'Товаров'})
        subcat_analysis['Отзывы'] = round(subcat_analysis['Отзывы'], 2)
        subcat_analysis['Средний рейтинг'] = round(subcat_analysis['Средний рейтинг'], 2)
        subcat_analysis['Цена'] = round(subcat_analysis['Цена'], 1)

        subcat_analysis_ = df_area[df_area['Продаж'] > 0].groupby(['Category_2', 'Category_3'],
                                                                      as_index=False).agg({'unique_id': 'nunique'
                                                                                           }).rename(
            columns={'unique_id': 'Товаров с продажами'})
        subcat_analysis = subcat_analysis.merge(subcat_analysis_, on=['Category_2', 'Category_3'], how='left')
        subcat_analysis['Товаров с продажами'] = subcat_analysis['Товаров с продажами'].fillna(0)
        subcat_analysis['Процент товаров с продажами'] = (
                subcat_analysis['Товаров с продажами'] / subcat_analysis['Товаров'] * 100).astype(int)
        subcat_analysis['Среднее число продаж на 1 товар'] = subcat_analysis['Продаж'] / subcat_analysis['Товаров']
        subcat_analysis['Среднее число продаж на 1 товар с продажами'] = np.where(
            subcat_analysis['Товаров с продажами'] == 0, 0,
            subcat_analysis['Продаж'] / subcat_analysis['Товаров с продажами'])
        subcat_analysis['Среднее число продаж на 1 товар'] = round(subcat_analysis['Среднее число продаж на 1 товар'],
                                                                   0).astype(int)
        subcat_analysis['Среднее число продаж на 1 товар с продажами'] = round(
            subcat_analysis['Среднее число продаж на 1 товар с продажами'], 0).astype(int)

        subcat_analysis = subcat_analysis.merge(main.groupby(['Category_2', 'Category_3'], as_index=False).agg({
            'merchantId': 'nunique'}).rename(columns={'merchantId': 'Число селлеров'}),
                                                on=['Category_2', 'Category_3'], how='left')

        subcat_analysis = subcat_analysis.merge(
            main[main['Продажи'] > 0].groupby(['Category_2', 'Category_3'], as_index=False).agg(
                {'merchantId': 'nunique'}).rename(columns={'merchantId': 'Селлеров с продажами'}),
            on=['Category_2', 'Category_3'], how='left')
        subcat_analysis['Селлеров с продажами'] = subcat_analysis['Селлеров с продажами'].fillna(0)
        subcat_analysis['Процент селлеров с продажами'] = np.where(
            ((subcat_analysis['Селлеров с продажами'].isna()) | (subcat_analysis['Число селлеров'].isna()) |
             (subcat_analysis['Число селлеров'] == 0)), 0,
             subcat_analysis['Селлеров с продажами'] / subcat_analysis['Число селлеров'] * 100)

        subcat_analysis['Процент селлеров с продажами'] = round(subcat_analysis['Процент селлеров с продажами'], 0).astype(int)

        subcat_analysis = subcat_analysis.merge(main.groupby(['Category_2', 'Category_3'], as_index=False).agg({
            'brand_id': 'nunique'}).rename(columns={'brand_id': 'Число брендов'}),
                                                on=['Category_2', 'Category_3'], how='left')

        subcat_analysis = subcat_analysis.merge(
            main[main['Продажи'] > 0].groupby(['Category_2', 'Category_3'], as_index=False).agg(
                {'brand_id': 'nunique'}).rename(columns={'brand_id': 'Брендов с продажами'}),
            on=['Category_2', 'Category_3'], how='left')
        subcat_analysis['Брендов с продажами'] = subcat_analysis['Брендов с продажами'].fillna(0)
        subcat_analysis['Процент брендов с продажами'] = round(
            subcat_analysis['Брендов с продажами'] / subcat_analysis['Число брендов'] * 100, 0).astype(int)
        subcat_analysis['Средняя выручка на 1 товар'] = subcat_analysis['Выручка'] / subcat_analysis['Товаров']
        subcat_analysis['Средняя выручка на 1 товар с продажами'] = np.where(
            subcat_analysis['Товаров с продажами'] == 0, 0,
            subcat_analysis['Выручка'] / subcat_analysis[
                'Товаров с продажами'])
        subcat_analysis['Средняя выручка на 1 товар'] = round(subcat_analysis['Средняя выручка на 1 товар'], 0).astype(
            int)
        subcat_analysis['Средняя выручка на 1 товар с продажами'] = round(
            subcat_analysis['Средняя выручка на 1 товар с продажами'], 0).astype(int)

        return subcat_analysis.to_dict('records'), \
               [{"name": i, "id": i, "deletable": True, "selectable": True} for i in subcat_analysis.columns]

    elif selector_drop == 'Бренд':
        brand_analysis = df_area.groupby(['Бренд'], as_index=False).agg(
            {'Средний рейтинг': 'mean',
             'Отзывы': 'mean',
             'Продаж': 'sum',
             'Выручка': 'sum',
             'Цена': 'mean',
             'unique_id': 'nunique'
             }).rename(columns={'unique_id': 'Товаров'})
        brand_analysis['Отзывы'] = round(brand_analysis['Отзывы'], 2)
        brand_analysis['Средний рейтинг'] = round(brand_analysis['Средний рейтинг'], 2)
        brand_analysis['Цена'] = round(brand_analysis['Цена'], 1)
        brand_analysis_ = df_area[df_area['Продаж'] > 0].groupby(['Бренд'], as_index=False).agg(
            {'unique_id': 'nunique'}).rename(
            columns={'unique_id': 'Товаров с продажами'})
        brand_analysis = brand_analysis.merge(brand_analysis_, on=['Бренд'], how='left')
        brand_analysis['Товаров с продажами'] = brand_analysis['Товаров с продажами'].fillna(0)
        brand_analysis['Процент товаров с продажами'] = (
                brand_analysis['Товаров с продажами'] / brand_analysis['Товаров'] * 100).astype(int)
        brand_analysis['Среднее число продаж на 1 товар'] = brand_analysis['Продаж'] / brand_analysis['Товаров']
        brand_analysis['Среднее число продаж на 1 товар с продажами'] = np.where(
            brand_analysis['Товаров с продажами'] == 0, 0,
            brand_analysis['Продаж'] / brand_analysis['Товаров с продажами'])
        brand_analysis['Среднее число продаж на 1 товар'] = round(brand_analysis['Среднее число продаж на 1 товар'],
                                                                  0).astype(int)
        brand_analysis['Среднее число продаж на 1 товар с продажами'] = round(
            brand_analysis['Среднее число продаж на 1 товар с продажами'], 0).astype(int)

        brand_analysis = brand_analysis.merge(main.groupby(['brand_name'], as_index=False).agg({
            'merchantId': 'nunique'}).rename(columns={'merchantId': 'Число селлеров'}),
                                              left_on=['Бренд'], right_on='brand_name', how='left').drop(['brand_name'], axis=1)

        brand_analysis = brand_analysis.merge(
            main[main['Продажи'] > 0].groupby(['brand_name'], as_index=False).agg(
                {'merchantId': 'nunique'}).rename(columns={'merchantId': 'Селлеров с продажами'}),
            left_on=['Бренд'], right_on='brand_name', how='left').drop(['brand_name'], axis=1)
        brand_analysis['Селлеров с продажами'] = brand_analysis['Селлеров с продажами'].fillna(0)
        brand_analysis['Процент селлеров с продажами'] = np.where(
            ((brand_analysis['Селлеров с продажами'].isna()) | (brand_analysis['Число селлеров'].isna()) |
             (brand_analysis['Число селлеров'] == 0)), 0,
             brand_analysis['Селлеров с продажами'] / brand_analysis['Число селлеров'] * 100)

        brand_analysis['Процент селлеров с продажами'] = round(brand_analysis['Процент селлеров с продажами'], 0).astype(int)


        brand_analysis['Средняя выручка на 1 товар'] = brand_analysis['Выручка'] / brand_analysis['Товаров']
        brand_analysis['Средняя выручка на 1 товар с продажами'] = np.where(brand_analysis['Товаров с продажами'] == 0,
                                                                            0,
                                                                            brand_analysis['Выручка'] / brand_analysis[
                                                                                'Товаров с продажами'])
        brand_analysis['Средняя выручка на 1 товар'] = round(brand_analysis['Средняя выручка на 1 товар'], 0).astype(
            int)
        brand_analysis['Средняя выручка на 1 товар с продажами'] = round(
            brand_analysis['Средняя выручка на 1 товар с продажами'], 0).astype(int)

        return brand_analysis.to_dict('records'), \
               [{"name": i, "id": i, "deletable": True, "selectable": True} for i in brand_analysis.columns]

    elif selector_drop == 'Тренд':
        new_main = main[(main['Category_1'] == category_1) & (main['Category_2'] == category_2)][
            ['unique_id', 'load_date', 'images', 'url', 'name', 'Category_1', 'Category_2', 'Category_3',
             'categoryName', 'brand_name', 'availableQuantity',
             'RewiewsCount', 'averageRating', 'sellingPrice', 'discountedPrice']].drop_duplicates()
        available_product = \
            main[(main['Category_1'] == category_1) & (main['Category_2'] == category_2)].groupby(
                ['unique_id'], as_index=False)['positive_availableQuantity'].sum()

        sales_product = main[(main['Category_1'] == category_1) & (main['Category_2'] == category_2)].groupby(
            ['unique_id'], as_index=False)['Продажи'].sum()
        revenue_product = main[(main['Category_1'] == category_1) & (main['Category_2'] == category_2)].groupby(
            ['unique_id'], as_index=False)['Выручка'].sum()

        new_main = new_main.merge(available_product, on='unique_id', how='left').merge(
            sales_product, on='unique_id', how='left').merge(
            revenue_product, on='unique_id', how='left')

        new_main.columns = ['unique_id', 'День', 'Фото', 'Ссылка', 'Название', 'Category_1', 'Category_2',
                            'Category_3', 'categoryName', 'Бренд',
                            'Наличие', 'Отзывы', 'Средний рейтинг', 'Цена',
                            'Цена со скидкой', 'Был в наличии', 'Продаж', 'Выручка']

        new_main['Выручка'] = round(new_main['Выручка'], 0).astype(int)
        new_main['Отзывы'] = round(new_main['Отзывы'], 0).astype(int)
        new_main['Наличие'] = new_main['Наличие'].fillna(0)
        new_main['Наличие'] = round((new_main['Наличие']), 0).astype(int)
        new_main['Был в наличии'] = round((new_main['Был в наличии']), 0).astype(int)
        new_main['Средний рейтинг'] = round(new_main['Средний рейтинг'], 2)
        # !!!!!!!
        # new_main = new_main.head(500)

        trend_analysis = new_main.groupby(['День'], as_index=False).agg(
            {'Продаж': 'sum',
             'Выручка': 'sum',
             'unique_id': 'nunique'
             }).rename(columns={'unique_id': 'Товаров'})
        trend_analysis_ = new_main[new_main['Продаж'] > 0].groupby(['День'],
                                                                   as_index=False).agg({'unique_id': 'nunique'
                                                                                        }).rename(
            columns={'unique_id': 'Товаров с продажами'})
        trend_analysis = trend_analysis.merge(trend_analysis_, on=['День'], how='left')
        trend_analysis['Товаров с продажами'] = trend_analysis['Товаров с продажами'].fillna(0)

        trend_analysis = trend_analysis.merge(main.groupby(['load_date'], as_index=False).agg({
            'merchantId': 'nunique'}).rename(columns={'merchantId': 'Число селлеров'}),
                                              left_on=['День'], right_on=['load_date'], how='left').drop(['load_date'],
                                                                                                         axis=1)

        trend_analysis = trend_analysis.merge(
            main[main['Продажи'] > 0].groupby(['load_date'], as_index=False).agg(
                {'merchantId': 'nunique'}).rename(columns={'merchantId': 'Селлеров с продажами'}),
            left_on=['День'], right_on=['load_date'], how='left').drop(['load_date'], axis=1)
        trend_analysis['Селлеров с продажами'] = trend_analysis['Селлеров с продажами'].fillna(0)

        trend_analysis = trend_analysis.merge(main.groupby(['load_date'], as_index=False).agg({
            'brand_id': 'nunique'}).rename(columns={'brand_id': 'Число брендов'}),
                                              left_on=['День'], right_on=['load_date'], how='left').drop(['load_date'],
                                                                                                         axis=1)
        trend_analysis = trend_analysis.merge(
            main[main['Продажи'] > 0].groupby(['load_date'], as_index=False).agg(
                {'brand_id': 'nunique'}).rename(columns={'brand_id': 'Брендов с продажами'}),
            left_on=['День'], right_on=['load_date'], how='left').drop(['load_date'], axis=1)
        trend_analysis['Брендов с продажами'] = trend_analysis['Брендов с продажами'].fillna(0)

        trend_analysis['Выручка на товар'] = np.where(
            ((trend_analysis['Выручка'].isna()) | (trend_analysis['Товаров с продажами'].isna()) |
             (trend_analysis['Товаров с продажами'] == 0)), 0,
             trend_analysis['Выручка'] / trend_analysis['Товаров с продажами'])
        trend_analysis['Выручка на товар'] = round(trend_analysis['Выручка на товар'], 0).astype(int)

        return trend_analysis.to_dict('records'), \
               [{"name": i, "id": i, "deletable": True, "selectable": True} for i in trend_analysis.columns]

    elif selector_drop == 'Ценовая сегментация':
        df_prices = main[(main['Category_1'] == category_1) & (main['Category_2'] == category_2)].drop_duplicates()
        days_all = main['load_date'].nunique()
        days_instock = df_prices[(df_prices['Товары в движении'] > 0)]['load_date'].nunique()

        df_prices['price_bucket'] = pd.qcut(df_prices['sellingPrice'], input_segm, duplicates='drop')

        df_prices_group = df_prices.groupby('price_bucket').agg(
            {
                'Продажи': 'sum',
                'Выручка': 'sum',
                'unique_id': 'nunique',
                'brand_id': 'nunique',
                'merchantId': 'nunique'
            }).rename(columns={'unique_id': 'Товаров', 'brand_id': 'Брендов', 'merchantId': 'Селлеров'})

        df_prices_t = df_prices[df_prices['Продажи'] > 0].groupby('price_bucket', as_index=False).agg(
            {'unique_id': 'nunique',
             'brand_id': 'nunique',
             'merchantId': 'nunique'}).rename(
            columns={'unique_id': 'Товаров с продажами', 'brand_id': 'Брендов с продажами',
                     'merchantId': 'Селлеров с продажами'})

        df_prices_group = df_prices_group.merge(df_prices_t, on='price_bucket', how='left')

        df_prices_group['Выручка на товар'] = np.where(
            df_prices_group['Товаров с продажами'] == 0, 0,
            df_prices_group['Выручка'] / df_prices_group['Товаров с продажами'])

        df_prices_group['От'] = df_prices_group['price_bucket'].apply(lambda x: x.left)
        df_prices_group['До'] = df_prices_group['price_bucket'].apply(lambda x: x.right)
        df_prices_group['Потенциал'] = df_prices_group['Выручка'] / days_instock * days_all
        df_prices_group['Потенциал'] = round(df_prices_group['Потенциал'], 0).astype(int)
        df_prices_group['Упущенная выручка'] = df_prices_group['Потенциал'] - df_prices_group['Выручка']
        df_prices_group['Упущенная выручка'] = round(df_prices_group['Упущенная выручка'], 0).astype(int)
        df_prices_group['Упущенная выручка %'] = np.where(df_prices_group['Потенциал']==0, 0,
            df_prices_group['Упущенная выручка'] / df_prices_group['Потенциал'] * 100)

        df_prices_group = df_prices_group[['От', 'До', 'Продажи', 'Выручка', 'Потенциал', 'Упущенная выручка',
                                           'Упущенная выручка %', 'Товаров', 'Товаров с продажами', 'Брендов',
                                           'Брендов с продажами',
                                           'Селлеров', 'Селлеров с продажами', 'Выручка на товар']]

        df_prices_group['Выручка'] = round(df_prices_group['Выручка'], 0).astype(int)
        df_prices_group['Выручка на товар'] = round(df_prices_group['Выручка на товар'], 0).astype(int)
        df_prices_group['От'] = round(df_prices_group['От'].astype(float), 0).astype(int)
        df_prices_group['До'] = round(df_prices_group['До'].astype(float), 0).astype(int)
        df_prices_group['Упущенная выручка %'] = round(df_prices_group['Упущенная выручка %'], 0)

        return df_prices_group.to_dict('records'), [{"name": i, "id": i, "deletable": True, "selectable": True} for i in
                                                    df_prices_group.columns]
'''
@app.callback(
    [Output('input_min', 'value'),
    Output('input_max', 'value')],
    Input('selector_drop', 'value'),
    [Input('subcat_table', 'data'),
     Input('subcat_table', 'columns')])
def set_slider(selector_drop, rows, columns):
    if selector_drop == 'Ценовая сегментация':
        df_slider = pd.DataFrame(rows, columns=[c['name'] for c in columns])
'''


@app.callback(
    Output('pie_graph', 'figure'), [Output(component_id='range_slider', component_property='min'),
     Output(component_id='range_slider', component_property='max')],

    [Input('subcat_table', 'data'),
     Input('subcat_table', 'columns')],
    Input('selector_drop', 'value'),
    Input('graph_selector', 'value'),
    Input('category_2', 'value')
    )

def display_firstgraph(rows, columns, selector_drop, graph_selector, category_2):
    # print('row', rows)
    # print('columns', columns)
    subcat_analysis_gr = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    colors_graph = ['gold', 'mediumturquoise', 'lightgreen']
    fig = go.Figure()
    if selector_drop == 'Тренд':
        #fig = make_subplots(specs=[[{"secondary_y": True}]])
        for val in graph_selector:
            # print(val, 'selector_trend')
            fig.add_trace(
                go.Scatter(x=subcat_analysis_gr['День'].values, y=subcat_analysis_gr[val].values,
                           name=val, fill='tonexty',#secondary_y=True,
                           mode='lines+markers'
                           ))
        return fig, 0, 0
    elif (selector_drop == 'Category_3') or (selector_drop == 'Бренд'):
        fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
        # print(selector_drop)
        labels = subcat_analysis_gr[selector_drop].values
        values1 = subcat_analysis_gr['Продаж'].values
        values2 = subcat_analysis_gr['Выручка'].values
        fig.add_trace(go.Pie(labels=labels, values=values1, name="Продажи", hole=0.4),
                      1, 1)
        fig.add_trace(go.Pie(labels=labels, values=values2, name="Выручка", hole=0.4),
                      1, 2)
        fig.update_traces(hoverinfo='label+percent', textinfo=None, textfont_size=20, textposition='inside',
                          marker=dict(colors=colors_graph, line=dict(color='#000000', width=2)))
        if selector_drop == 'Category_3':
            fig.update_layout(title_text="Аналитика по Category_3",
                              annotations=[dict(text='Продажи', x=0.17, y=0.5, font_size=20, showarrow=False),
                                           dict(text='Выручка', x=0.84, y=0.5, font_size=20, showarrow=False)])
        elif selector_drop == 'Бренд':
            fig.update_layout(title_text="Аналитика по Брендам",
                              annotations=[dict(text='Продажи', x=0.17, y=0.5, font_size=20, showarrow=False),
                                           dict(text='Выручка', x=0.82, y=0.5, font_size=20, showarrow=False)])

        return fig, 0, 0

    elif selector_drop == 'Ценовая сегментация':
        subcat_analysis_gr['segments'] = subcat_analysis_gr['От'].astype(str) + ' - ' + subcat_analysis_gr['До'].astype(str)

        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Bar(x=subcat_analysis_gr['segments'].values,
                   y=subcat_analysis_gr['Продажи'].values,
                   name='Продажи', marker_color='lightsalmon', offsetgroup=1), secondary_y=False
                       )
        fig.add_trace(
            go.Bar(x=subcat_analysis_gr['segments'].values,
                   y=subcat_analysis_gr['Выручка'].values,
                   name='Выручка', marker_color='#81F573', offsetgroup=2), secondary_y=True
                   )
        
        fig.update_yaxes(color='#EB9154', secondary_y=False)
        fig.update_yaxes(color='#0AF573', secondary_y=True)
        fig.update_layout(title_text=f"Ценовая сегментация по {category_2}", barmode='group',
                          bargroupgap=0.1)


        return fig, subcat_analysis_gr['От'].min(), subcat_analysis_gr['До'].max()

'''
@app.callback([Output('input_min', 'value'),
               Output('input_max', 'value')],
              [Input(component_id='range_slider', component_property='min'),
              Input(component_id='range_slider', component_property='max')])
def set_inputs(min_slider, max_slider):
    return min_slider, max_slider
'''

@app.callback(
    Output("input_min", "value"),
    Output("input_max", "value"),
    Output("range_slider", "value"),
    Input("range_slider", "value"),
    [Input(component_id='range_slider', component_property='min'),
    Input(component_id='range_slider', component_property='max')]
)
def callback(slider, min_slider, max_slider):
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    start_value = min_slider if trigger_id == "input_min" else slider[0]
    end_value = max_slider if trigger_id == "input_max" else slider[1]
    slider_value = slider if trigger_id == "range_slider" else [start_value, end_value]

    return start_value, end_value, slider_value


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8000, debug=True)
    # app.run_server(debug=True)

# bokeh sample codes
#from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.palettes import Viridis3
from bokeh.plotting import figure
from read_csv_to_pandas import *
from bokeh.charts import Scatter, output_file, show

def get_stock_data(stock_id_list,all): # all= True or False
    data=get_one_stock_whole_data(stock_id_list,all)
    return data

def display_stock_info(stock_info): #stock_info={"stock_id":..."stock_info":....}
    output_file("stock_data_displayer.html")

    for item in stock_info:
        stock_id=item["stock_id"]
        stock_price_info=item["stock_info"]
        date_data=stock_price_info["date"]
        open_price=stock_price_info["open"]
        high_price=stock_price_info["high"]
        low_price=stock_price_info["low"]
        close_price=stock_price_info["close"]
        volume_data=stock_price_info["volume"]
        adj_v_data=stock_price_info["_adj_close"]

        p = Scatter(stock_price_info, x='date', y="open",title=stock_id+" price data", legend="top_left",xlabel="date", ylabel="open price")
        show(p)

        open_f=figure()
        high_f=figure()
        low_f=figure()
        close_f=figure()
        volume_f=figure()
        adj_v_f=figure()


def plot_test():
    output_file("layout_grid_convenient.html")

    x = list(range(11))
    y0 = x
    y1 = [10 - i for i in x]
    y2 = [abs(i - 5) for i in x]

    # create three plots
    s1 = figure()
    s1.circle(x, y0, size=10, color=Viridis3[0])
    s2 = figure()
    s2.triangle(x, y1, size=10, color=Viridis3[1])
    s3 = figure()
    s3.square(x, y2, size=10, color=Viridis3[2])

    # make a grid
    grid = gridplot([s1, s2, s3], ncols=2, plot_width=250, plot_height=250)

    # show the results
    show(grid)

def main():
    stock_info=get_stock_data(["1419"],False)
    """
    item=stock_info[0]
    stock_id=item["stock_id"]
    stock_price_info=item["stock_info"]
    date_data=stock_price_info["date"]
    open_price=stock_price_info["open"]
    high_price=stock_price_info["high"]
    low_price=stock_price_info["low"]
    close_price=stock_price_info["close"]
    volume_data=stock_price_info["volume"]
    adj_v_data=stock_price_info["_adj_close"]

    print(stock_id)
    print(date_data)
    print(open_price)
    print(high_price)
    print(low_price)
    print(close_price)
    print(volume_data)
    print(adj_v_data)
    """
    display_stock_info(stock_info)
    #plot_test()
    print("not implemented!!")


if __name__=="__main__":
    main()

@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_trade(item_id):
    trade = Trade.query.get_or_404(item_id)

    if request.method == "POST":
        trade.representative = request.form.get("representative", "").strip()
        trade.trade_date = request.form.get("trade_date", "").strip()
        trade.disclosure_date = request.form.get("disclosure_date", "").strip()
        trade.ticker = request.form.get("ticker", "").strip()
        trade.asset_type = request.form.get("asset_type", "").strip()
        trade.transaction_type = request.form.get("transaction_type", "").strip()
        trade.amount_min = request.form.get("amount_min", "").strip()
        trade.amount_max = request.form.get("amount_max", "").strip()
        trade.source = request.form.get("source", "").strip()

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit_trade.html", trade=trade)
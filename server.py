import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


competitions = load_competitions()
clubs = load_clubs()

app = Flask(__name__)
app.secret_key = 'something_special'


@app.route('/')
def index():
    return render_template('points_board.html', clubs=clubs)


@app.route('/authen')
def authen():
    return render_template('index.html')


@app.route('/show_summary', methods=['POST'])
def show_summary():
    """ function that permits the authentification of a user"""
    if request.form['email'] == "":
        flash("Empty Email, please try again")
        return render_template('index.html')
    clubs_list = []
    for club in clubs:
        if club['email'] == request.form['email']:
            clubs_list.append(club)
            return render_template(
                'welcome.html',
                club=club,
                competitions=competitions)
    if clubs_list == []:
        flash('Unknown user')
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    the_actual_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [
        c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        if found_competition["date"] < the_actual_date:
            flash("You can t book a past competition")
            return render_template(
                'welcome.html',
                club=found_club,
                competitions=competitions)
        else:
            return render_template(
                'booking.html',
                club=found_club,
                competition=found_competition,
                )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html', club=club, competitions=competitions)


@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    competition = [
        c for c in competitions if c['name'] == request.form['competition']][0]
    club = [
        c for c in clubs if c['name'] == request.form['club']][0]
    pt_allow = int(request.form['points'])
    pl_req = int(request.form['places'])
    if pl_req <= pt_allow:
        if pl_req > 12:
            flash('You can t book over 12 points')
            pl_req = 12
        competition['number_of_places'] = int(competition[
            'number_of_places'])-pl_req
        flash('Great-booking complete!')
        club['points'] = pt_allow-pl_req
    else:
        flash('this club doesn t have enought points for booking')
    return render_template(
       'welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()

import React, {Component, PropTypes} from 'react';

import 'whatwg-fetch';
import * as Cookies from 'js-cookie';


class ThoughtForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            conditions: [],
            chosen_condition: null,
            notes: null
        };
    }

    componentDidMount = () => {
        let _this = this;
        fetch(
            '/api/conditions.json', {
                credentials: 'same-origin'
            }
        ).then(function(response) {
            return response.json()
        }).then(function(data) {
            _this.setState({conditions: data});
        });
    }

    onConditionChange = (e) => {
        this.setState({chosen_condition: e.target.value});
    }

    onNotesChange = (e) => {
        this.setState({notes: e.target.value});
    }

    onSubmit = (e) => {
        e.preventDefault();

        let csrf = Cookies.get('csrftoken');

       fetch(
           '/api/thoughts.json', {
               credentials: 'same-origin',
               method: 'POST',
               body: JSON.stringify({
                   condition: this.state.chosen_condition,
                   notes: this.state.notes || '',
               }),
               headers: {
                   'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Cache': 'no-cache',
                   'X-CSRFToken': csrf
               }
           }
       ).then((response) => {
           if (response.ok) {
               this.setState({chosen_condition: null, notes: null})
           }
           this.props.onThoughtsChange();
           return response;
       })
    }

    render() {
        return (
            <div>
                <h2>How are you feeling?</h2>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label className="control-label" htmlFor="id_condition">Condition</label>
                        <select name="condition" id="id_condition" required className="form-control" onChange={this.onConditionChange}>
                            <option value="">------------</option>
                        {this.state.conditions.map(condition =>
                            <option key={condition.key} value={condition.value} selected={this.state.chosen_condition == condition.value}>{condition.label}</option>
                        )}
                        </select>
                    </div>
                    <div className="form-group">
                        <label className="control-label" htmlFor="id_notes">Notes (optional)</label>
                        <textarea id="id_notes" name="notes" className="form-control" onChange={this.onNotesChange}>{this.state.notes}</textarea>
                    </div>
                    <div className="form-group">
                        <input type="submit" value="Record" className="btn btn-default"/>
                    </div>
                </form>
            </div>
        )
    }
}

module.exports = {'ThoughtForm': ThoughtForm}

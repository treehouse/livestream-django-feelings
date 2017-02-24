import React, {Component, PropTypes} from 'react';

import 'whatwg-fetch';

class Thought extends Component {
    constructor(props) {
        super(props);
        this.state = props.data;
    }
    render() {
        var date = new Date(this.state.recorded_at);
        console.log(date);
        return (
            <div className="list-group-item">
                <h4 className="list-group-item-heading">
                    <time className="pull-right small">{this.state.recorded_at}</time>
                    {this.state.condition_display}
                </h4>
                {this.state.notes}
            </div>
        )
    }
}

class RecentThoughts extends Component {
    constructor(props) {
        super(props);
        this.state = {thoughts: []};
    }
    componentDidMount() {
        let _this = this;
        fetch(
            '/api/thoughts.json', {
                credentials: 'same-origin'
            }
        ).then(function(response) {
            return response.json()
        }).then(function(data) {
            _this.setState({thoughts: data});
        });
    }
    render() {
        return (
            <div>
                <h2>Recent Thoughts</h2>
                <div className="list-group">
                    {this.state.thoughts.map(thought =>
                        <Thought key={thought.id} data={thought}/>
                    )}
                </div>
            </div>
        )
    }
}

module.exports = {'RecentThoughts': RecentThoughts}

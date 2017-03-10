import React, {Component, PropTypes} from 'react';

import 'whatwg-fetch';

class Thought extends Component {
    constructor(props) {
        super(props);
        this.state = props.data;
    }

    render() {
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
    componentDidMount() {
        this.props.onThoughtsChange();
    }

    render() {
        return (
            <div>
                <h2>Recent Thoughts</h2>
                <div className="list-group">
                    {this.props.thoughts.map(thought =>
                        <Thought key={thought.id} data={thought}/>
                    )}
                </div>
            </div>
        )
    }
}

module.exports = {'RecentThoughts': RecentThoughts}

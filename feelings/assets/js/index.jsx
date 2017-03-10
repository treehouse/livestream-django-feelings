import React from 'react';
import ReactDOM from 'react-dom';
import 'whatwg-fetch';

import { RecentThoughts } from './recent_thoughts';
import { ThoughtForm } from './thought_form';

class RootElement extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            thoughts: []
        }
    }

    updateThoughts = () => {
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
            <div className="row">
                <div className="col-md-6">
                    <RecentThoughts thoughts={this.state.thoughts} onThoughtsChange={this.updateThoughts}/>
                </div>
                <div className="col-md-6">
                    <ThoughtForm onThoughtsChange={this.updateThoughts}/>
                </div>
            </div>
        )
    }
}

ReactDOM.render(
    <RootElement/>,
    document.getElementById('react-app')
);


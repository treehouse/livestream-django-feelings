import React, { Component } from 'react';
import { Line } from 'react-chartjs';

class Chart extends Component {
    componentDidMount() {
        this.props.onThoughtsChange();
    }

    constructor(props) {
        super(props);
        this.state = {
        };
    }

    defineData = () => {
        let thoughts = this.props.thoughts || null;
        var data = {
            labels: ['', '', '', '', '', '', '', '', '', ''],
            datasets: [{
                label: "Feelings",
                fill: true
            }]
        };
        if (thoughts.length != 0) {
            data.labels = [];
            data.datasets[0].data = this.props.thoughts.map((thought) => { return thought.condition });
        }
        return data;
    }

    render() {
        return (
            <div>
                <Line data={this.defineData()} width="600" height="250"/>
            </div>
        )
    }
}

module.exports = {'Chart': Chart}

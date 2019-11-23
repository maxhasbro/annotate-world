import { createStore } from 'redux'
import { annotateWorldApp } from '../reducers/reducers'

const store = createStore(annotateWorldApp);
odoo.define('loss_product.models', function (require) {
  "use strict";

var models = require('point_of_sale.models');
var core = require('web.core');
var utils = require('web.utils');

var round_pr = utils.round_precision;

var _t = core._t;

models.load_fields('product.product','loss_product');

});

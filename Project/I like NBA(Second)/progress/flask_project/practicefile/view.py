import pandas as pd
import pymysql
from flask import Flask, request, render_template, redirect, url_for


def get_context_data(self, **kwargs):
    context = super(PostLV, self).get_context_data(**kwargs)
    paginator = context['paginator']
    page_numbers_range = 10
    max_index = len(paginator.page_range)

    page = self.request.GET.get('page')
    current_page = int(page) if page else 1

    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]
    context['page_range'] = page_range
    return context

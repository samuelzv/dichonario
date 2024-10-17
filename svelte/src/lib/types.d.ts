export type QuoteListI18n = {
    search: string;
    new_quote: string;
    previous_page: string;
    next_page: string;
    page: string;
    from: string;
    edit: string;
    delete: string;
}

export type LanguageToggleI18n = {
  english_code: string;
  english_label: string;
  english_description: string;
  spanish_code: string;
  spanish_label: string;
  spanish_description: string;
}

export type Pagination = {
  current_page: number; 
  has_next: boolean; 
  has_previous:  boolean; 
  num_pages: number; 
  total_records: number; 
  previous_page: number;
  next_page: number;
}

export type Quote = {
  id: string;
  quote: string;
  author__name: string;
  author__image: string;
  author__image_sm: string;
  author__image_md: string;
  author__image_lg: string;
  is_owner: boolean;
}

export type Quotes = Array<Quote>;
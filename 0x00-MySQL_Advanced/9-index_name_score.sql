-- Create an index idx_name_first_score on the first letter of the name and score.

CREATE INDEX idx_name_first_score ON names(name(1), score);

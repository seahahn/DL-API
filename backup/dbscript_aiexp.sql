CREATE TABLE ai_example(
	idx SERIAL NOT NULL, -- 게시물 고유 번호
	div VARCHAR(10) NOT NULL, -- 구분(ml / dl)
	image_src VARCHAR(255) NOT NULL,
	author VARCHAR(255) NOT NULL,
	category VARCHAR(255) NOT NULL,
	title VARCHAR(255) NOT NULL,
	dsc TEXT NOT NULL, -- description
	link VARCHAR(255) NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(), -- 생성 시점
	CONSTRAINT ai_example_pk PRIMARY KEY (idx)
);
COMMENT ON TABLE ai_example IS 'AI Play 인공지능 체험용 프로젝트들의 정보';

-- Column comments

COMMENT ON COLUMN ai_example.idx IS '게시물 고유 번호';
COMMENT ON COLUMN ai_example.div IS '게시물 구분 값(ML / DL)';
COMMENT ON COLUMN ai_example.image_src IS '대표 사진 S3 URL';
COMMENT ON COLUMN ai_example.author IS '제작자';
COMMENT ON COLUMN ai_example.category IS '세분류(DL이면 CV or NLP 등)';
COMMENT ON COLUMN ai_example.title IS '게시물 제목';
COMMENT ON COLUMN ai_example.dsc IS 'description. 간단한 설명글';
COMMENT ON COLUMN ai_example.link IS 'ML:게시물 이동 링크 / DL:해당 기능 이동 링크';
COMMENT ON COLUMN ai_example.created_at IS '가입 시점';
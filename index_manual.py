from pdf_rag import PDFEnhancementPipeline
import logging
import os

# 初始化 logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# 設定 OpenAI 金鑰（環境變數或直接填入）
api_key = os.environ.get("OPENAI_API_KEY", "sk-youropenaikey")

# 建立 pipeline
pipeline = PDFEnhancementPipeline(
    openai_api_key=api_key,
    logger=logger,
    embedding_type="openai",
    persist_directory="./chroma_db"
)

# 手冊路徑
#markdown_path = "data/CarbonInventory_AI_manual.md"

markdown_path = "data/CarbonInventory_AI_manual_updated.md"

# 執行 index（索引）
pipeline.rag_engine.index_document(
    document_path=markdown_path,
    document_type="markdown",
    mode="overwrite",  # 或 append
    metadata={"source": "carbon_inventory_manual"}
)

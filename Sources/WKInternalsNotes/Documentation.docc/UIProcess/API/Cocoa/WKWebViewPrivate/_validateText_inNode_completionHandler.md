# ``WKInternalsNotes/WKWebView/_validateText(_:inNode:completionHandler:)``

抽出テキストを OCR で検証する。

## Objective-C Declaration
```objective-c
- (void)_validateText:(const String&)text inNode:(std::optional<WebCore::NodeIdentifier>&&)nodeIdentifier completionHandler:(CompletionHandler<void(const String&)>&&)completionHandler;
```

## Discussion
- `text` が空ならそのまま返す。
- `_textValidationCache` にヒットした場合は cached 結果を返す。
- 未キャッシュの場合は抽出テキストのスナップショットを取り、`recognizeText` で OCR を実行する。
- `computeSimilarity` が閾値を下回る場合は認識結果を返し、十分近ければ元のテキストを返す。
- `ENABLE(TEXT_EXTRACTION_FILTER)` 有効時のみコンパイルされる。

## References
- [`WKWebView.mm#L333`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L333)
- [`WKWebView.mm#L333`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L333)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

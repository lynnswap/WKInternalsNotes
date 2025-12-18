# ``WKInternalsNotes/WKPreferences/_textExtractionEnabled``

Text Extraction を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTextExtractionEnabled:) BOOL _textExtractionEnabled WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
iOS: `NO` / macOS: `NO` / visionOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_textExtractionEnabled = YES`: `WKWebView` の `_performInteraction:completionHandler:` が `textExtractionEnabled()` チェックで reject されなくなる。
- `_textExtractionEnabled = NO`: `_performInteraction:completionHandler:` が `"Text extraction is unavailable"` を返して終了する。
- Implementation: [[[`Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm) の `_performInteraction:completionHandler:` が `textExtractionEnabled()` をチェックする。

## Details
- WebPreferences key: `TextExtractionEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L137)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L848`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L848)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7909`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7909) (key: `TextExtractionEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

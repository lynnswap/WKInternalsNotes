# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_corsDisablingPatterns``

CORS 無効化パターン

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCORSDisablingPatterns:) NSArray<NSString *> *_corsDisablingPatterns WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
iOS: `[]` / macOS: `[]`

## Discussion
- この API を使わない場合: パターンが空のため、CORS は通常どおり有効。
- `_corsDisablingPatterns` を設定すると: マッチしたパターンに対して CORS を無効化する（主にテスト/拡張機能向け）。
- 空配列に戻すと: 通常どおり CORS が有効になる。

## Details
- empty 配列

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L103)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1085`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1085)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

# ``WKInternalsNotes/WKWebViewConfiguration/_processDisplayName``

Web process の表示名

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setProcessDisplayName:) NSString *_processDisplayName WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: 表示名は既定のまま（`nil`）。
- `_processDisplayName` を設定すると: Web content process の表示名としてその文字列が使われる（主にログ/診断向け）。
- `nil` に戻すと: 既定の表示名に戻る。

## Details
- null 文字列は `nil` として返る

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L150)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1502`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1502)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

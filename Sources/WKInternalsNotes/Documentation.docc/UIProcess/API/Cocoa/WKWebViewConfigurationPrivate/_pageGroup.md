# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_pageGroup``

旧 `WKPageGroupRef`（互換のための API）

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setPageGroup:) WKPageGroupRef _pageGroup WK_API_DEPRECATED_WITH_REPLACEMENT("_groupIdentifier", macos(10.13.4, 14.2));
```

## Default Value
macOS: `nullptr`

## Discussion
- この API を使わない場合: `WKPageGroupRef` は利用されず、browsing context group は `_groupIdentifier` など別経路に従う。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない（常に `nullptr`）。

## Details
- 実装は no-op（常に `nullptr`）

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L132)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1300`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1300)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

# ``WKInternalsNotes/WKWebViewConfiguration/_multiRepresentationHEICInsertionEnabled``

`NSAdaptiveImageGlyph`（multi-representation HEIC）の挿入を許可する

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMultiRepresentationHEICInsertionEnabled:) BOOL _multiRepresentationHEICInsertionEnabled WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_multiRepresentationHEICInsertionEnabled = YES`: WebView が editable でなくても、page が richly editable な場合に `supportsAdaptiveImageGlyph` が `YES` になり、挿入が有効になる。
- `_multiRepresentationHEICInsertionEnabled = NO`: WebView が editable でない場合は `supportsAdaptiveImageGlyph` が `NO` になり、挿入が無効になる。

## Details
- `ENABLE(MULTI_REPRESENTATION_HEIC)` が無効なら常に `NO`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L174`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L174)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L266`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L266)
- [`Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14195)
- [`Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1131)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

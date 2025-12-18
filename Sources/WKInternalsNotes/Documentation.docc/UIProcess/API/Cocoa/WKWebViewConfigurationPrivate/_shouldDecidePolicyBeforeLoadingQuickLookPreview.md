# ``WKInternalsNotes/WKWebViewConfiguration/_shouldDecidePolicyBeforeLoadingQuickLookPreview``

Quick Look preview の読み込み前に policy 決定

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldDecidePolicyBeforeLoadingQuickLookPreview:) BOOL _shouldDecidePolicyBeforeLoadingQuickLookPreview WK_API_AVAILABLE(ios(13.0));
```

## Default Value
iOS: `USE(QUICK_LOOK) ? linkedOnOrAfterSDKWithBehavior(SDKAlignedBehavior::DecidesPolicyBeforeLoadingQuickLookPreview) : NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldDecidePolicyBeforeLoadingQuickLookPreview = YES`: Quick Look preview の読み込み前に policy 決定。
- `_shouldDecidePolicyBeforeLoadingQuickLookPreview = NO`: Quick Look preview の読み込み前に policy 決定（無効）。

## Details
- SDK 依存

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L121)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L260`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L260)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

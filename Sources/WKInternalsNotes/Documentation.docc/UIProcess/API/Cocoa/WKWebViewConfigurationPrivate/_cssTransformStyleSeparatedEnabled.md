# ``WKInternalsNotes/WKWebViewConfiguration/_cssTransformStyleSeparatedEnabled``

separated layers の `transform-style`

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCSSTransformStyleSeparatedEnabled:) BOOL _cssTransformStyleSeparatedEnabled WK_API_AVAILABLE(visionos(2.4));
```

## Default Value
visionOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_cssTransformStyleSeparatedEnabled = YES`: separated layers の `transform-style`。
- `_cssTransformStyleSeparatedEnabled = NO`: separated layers の `transform-style`（無効）。

## Details
- `HAVE(CORE_ANIMATION_SEPARATED_LAYERS)` が無効なら常に `NO`
- WebPreferences key: `CSSTransformStyleSeparatedEnabled`

## References
- [`WKWebViewConfigurationPrivate.h#L182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L182)
- [`WKWebViewConfiguration.mm#L269`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L269)
- [`APIPageConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIPageConfiguration.h)
- [`UnifiedWebPreferences.yaml#L1514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1514) (key: `CSSTransformStyleSeparatedEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

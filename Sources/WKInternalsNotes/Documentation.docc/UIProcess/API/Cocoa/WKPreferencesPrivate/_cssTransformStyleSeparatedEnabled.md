# ``WKInternalsNotes/WKPreferences/_cssTransformStyleSeparatedEnabled``

CSS transform-style: separated を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCSSTransformStyleSeparatedEnabled:) BOOL _cssTransformStyleSeparatedEnabled WK_API_AVAILABLE(visionos(2.4));
```

## Default Value
visionOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_cssTransformStyleSeparatedEnabled = YES`: CSS transform-style: separated を有効化する。
- `_cssTransformStyleSeparatedEnabled = NO`: CSS transform-style: separated を無効化する。
- Implementation: [`CSSParserContext.cpp#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/css/parser/CSSParserContext.cpp#L63) の `CSSParserContext::CSSParserContext` が `cssTransformStyleSeparatedEnabled()` を参照する。

## Details
- WebPreferences key: `CSSTransformStyleSeparatedEnabled`

## References
- [`WKPreferencesPrivate.h#L198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L198)
- [`WKPreferences.mm#L1670`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1670)
- [`CSSParserContext.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/css/parser/CSSParserContext.cpp)
- [`UnifiedWebPreferences.yaml#L1514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1514) (key: `CSSTransformStyleSeparatedEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

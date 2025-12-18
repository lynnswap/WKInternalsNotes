# ``WKInternalsNotes/WKPreferences/_modelNoPortalAttributeEnabled``

Model noportal attribute を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setModelNoPortalAttributeEnabled:) BOOL _modelNoPortalAttributeEnabled WK_API_AVAILABLE(visionos(2.4));
```

## Default Value
visionOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_modelNoPortalAttributeEnabled = YES`: Model noportal attribute を有効化する。
- `_modelNoPortalAttributeEnabled = NO`: Model noportal attribute を無効化する。
- Implementation: [`Source/WebCore/Modules/model-element/HTMLModelElement.cpp#L830`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/model-element/HTMLModelElement.cpp#L830) の `HTMLModelElement::attributeChanged` が `modelNoPortalAttributeEnabled()` を参照する。

## Details
- WebPreferences key: `ModelNoPortalAttributeEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L202)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1718`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1718)
- [`Source/WebCore/Modules/model-element/HTMLModelElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/model-element/HTMLModelElement.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5399`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5399) (key: `ModelNoPortalAttributeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

# ``WKInternalsNotes/_WKActivatedElementInfo/activatedElementInfoWithInteractionInformationAtPosition(_:userInfo:)``

位置情報から要素情報を生成する（iOS）。

## Objective-C Declaration
```objective-c
+ (instancetype)activatedElementInfoWithInteractionInformationAtPosition:(const WebKit::InteractionInformationAtPosition&)information userInfo:(NSDictionary *)userInfo;
```

## Discussion
`_initWithInteractionInformationAtPosition:isUsingAlternateURLForImage:userInfo:` を `isUsingAlternateURLForImage = NO` で呼び出し、autorelease して返す。

## References
- [`_WKActivatedElementInfoInternal.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L40)
- [`_WKActivatedElementInfo.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

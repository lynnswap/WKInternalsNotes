# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithType(_:URL:information:)``

指定 URL と位置情報から初期化する内部イニシャライザ。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithType:(_WKActivatedElementType)type URL:(NSURL *)url information:(const WebKit::InteractionInformationAtPosition&)information;
```

## Discussion
`information.imageURL` を使って `_initWithType:URL:imageURL:information:` に委譲する。

## References
- [`_WKActivatedElementInfoInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L42)
- [`_WKActivatedElementInfo.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L86)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

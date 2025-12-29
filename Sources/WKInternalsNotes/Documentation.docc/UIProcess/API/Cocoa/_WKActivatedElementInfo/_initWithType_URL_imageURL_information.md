# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithType(_:URL:imageURL:information:)``

URL と画像 URL を指定して初期化する内部イニシャライザ。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithType:(_WKActivatedElementType)type URL:(NSURL *)url imageURL:(NSURL *)imageURL information:(const WebKit::InteractionInformationAtPosition&)information;
```

## Discussion
`information.image` を使って `_initWithType:URL:imageURL:image:userInfo:information:` に委譲する。

## References
- [`_WKActivatedElementInfoInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L42)
- [`_WKActivatedElementInfo.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

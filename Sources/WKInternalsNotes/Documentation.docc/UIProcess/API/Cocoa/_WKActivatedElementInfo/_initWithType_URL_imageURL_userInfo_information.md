# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithType(_:URL:imageURL:userInfo:information:)``

指定されたURLと画像URL、ユーザー情報で初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithType:(_WKActivatedElementType)type URL:(NSURL *)url imageURL:(NSURL *)imageURL userInfo:(NSDictionary *)userInfo information:(const WebKit::InteractionInformationAtPosition&)information;
```

## Discussion
`information.image` を渡して下位イニシャライザへ委譲する。

## References
- [`_WKActivatedElementInfoInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L42)
- [`_WKActivatedElementInfo.mm#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L129)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

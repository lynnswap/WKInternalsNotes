# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithType(_:URL:image:information:)``

指定されたURLと画像で初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithType:(_WKActivatedElementType)type URL:(NSURL *)url image:(WebCore::ShareableBitmap*)image information:(const WebKit::InteractionInformationAtPosition&)information;
```

## Discussion
`information.imageURL` を用いて `imageURL` を補い、`userInfo` を `nil` にして下位イニシャライザへ委譲する。

## References
- [`_WKActivatedElementInfoInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L42)
- [`_WKActivatedElementInfo.mm#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L122)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

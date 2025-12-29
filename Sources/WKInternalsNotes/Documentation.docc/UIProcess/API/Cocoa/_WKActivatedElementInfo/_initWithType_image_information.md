# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithType(_:image:information:)``

指定された画像で初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithType:(_WKActivatedElementType)type image:(WebCore::ShareableBitmap*)image information:(const WebKit::InteractionInformationAtPosition&)information;
```

## Discussion
`information` からURLとimageURLを補い、`userInfo` を `nil` にして下位イニシャライザへ委譲する。

## References
- [`_WKActivatedElementInfoInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L42)
- [`_WKActivatedElementInfo.mm#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L112)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

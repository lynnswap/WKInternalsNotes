# ``WKInternalsNotes/_WKActivatedElementInfo/_isUsingAlternateURLForImage``

画像の代替URLを使用しているかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isUsingAlternateURLForImage;
```

## Default Value
`_initWithInteractionInformationAtPosition:isUsingAlternateURLForImage:userInfo:` の `isUsingAlternateURLForImage` で決まる。

## Discussion
初期化時に `_isUsingAlternateURLForImage` を設定し、getter で返す。

## References
- [`_WKActivatedElementInfoInternal.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L53)
- [`_WKActivatedElementInfo.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L95)
- [`_WKActivatedElementInfo.mm#L204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L204)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

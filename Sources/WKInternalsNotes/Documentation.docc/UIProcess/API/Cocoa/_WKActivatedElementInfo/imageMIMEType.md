# ``WKInternalsNotes/_WKActivatedElementInfo/imageMIMEType``

画像の MIME タイプを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *imageMIMEType;
```

## Default Value
`nil`（初期化時に設定される）。

## Discussion
`InteractionInformationAtPosition` の `imageMIMEType` を保持し、その値を返す。

## References
- [`_WKActivatedElementInfoInternal.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L47)
- [`_WKActivatedElementInfo.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

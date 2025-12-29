# ``WKInternalsNotes/_WKActivatedElementInfo/_isImage``

要素が画像かどうかを示す内部フラグ。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isImage;
```

## Default Value
`NO`（初期化時に設定される）。

## Discussion
`InteractionInformationAtPosition` の `isImage` を保持し、その値を返す。

## References
- [`_WKActivatedElementInfoInternal.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L52)
- [`_WKActivatedElementInfo.mm#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L236)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

# ``WKInternalsNotes/_WKActivatedElementInfo/ID``

要素の `id` 属性を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *ID WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
`nil`（初期化時に設定される）。

## Discussion
`InteractionInformationAtPosition` の `idAttribute` を保持し、その値を返す。

## References
- [`_WKActivatedElementInfo.h#L13`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L13)
- [`_WKActivatedElementInfo.mm#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L166)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

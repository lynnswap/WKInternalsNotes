# ``WKInternalsNotes/_WKActivatedElementInfo/URL``

要素に関連する URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *URL;
```

## Default Value
`nil`（初期化時に設定される）。

## Discussion
`InteractionInformationAtPosition` の `url` を保持し、その値を返す。

## References
- [`_WKActivatedElementInfo.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L44)
- [`_WKActivatedElementInfo.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L149)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

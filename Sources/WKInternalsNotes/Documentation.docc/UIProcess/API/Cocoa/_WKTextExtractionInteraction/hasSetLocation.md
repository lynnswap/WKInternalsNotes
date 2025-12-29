# ``WKInternalsNotes/_WKTextExtractionInteraction/hasSetLocation``

`location` が明示的に設定されたかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL hasSetLocation;
```

## Default Value
`NO`。

## Discussion
`setLocation:` が呼ばれると `YES` に設定される。初期状態は `NO`。

## References
- [`_WKTextExtraction.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L91)
- [`_WKTextExtractionInternal.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

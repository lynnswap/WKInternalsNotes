# ``WKInternalsNotes/_WKTextExtractionInteractionResult/error``

エラー情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSError *error;
```

## Default Value
`nil`（エラーがない場合）。

## Discussion
`initWithErrorDescription:` で設定された `NSError` を返す。

## References
- [`_WKTextExtraction.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L97)
- [`_WKTextExtraction.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L119)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |

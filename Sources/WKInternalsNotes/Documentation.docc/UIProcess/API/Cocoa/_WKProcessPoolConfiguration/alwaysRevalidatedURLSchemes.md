# ``WKInternalsNotes/_WKProcessPoolConfiguration/alwaysRevalidatedURLSchemes``

指定した URL スキームを常に再検証するよう設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<NSString *> *alwaysRevalidatedURLSchemes WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
未設定時は空配列を返す。

## Discussion
getter は `alwaysRevalidatedURLSchemes` のベクタを `NSArray` に変換して返し、setter は文字列配列を `Vector<String>` に変換して保存する。

## References
- [`_WKProcessPoolConfiguration.mm#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L186)
- [`_WKProcessPoolConfiguration.mm#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L191)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

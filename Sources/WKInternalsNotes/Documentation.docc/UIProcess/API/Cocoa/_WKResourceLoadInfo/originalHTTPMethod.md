# ``WKInternalsNotes/_WKResourceLoadInfo/originalHTTPMethod``

元の HTTP メソッド文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *originalHTTPMethod;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
内部の `ResourceLoadInfo` が保持する HTTP メソッドを `NSString` として返す。

## References
- [`_WKResourceLoadInfo.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L61)
- [`_WKResourceLoadInfo.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L118)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

# ``WKInternalsNotes/_WKDataTask/cancel()``

データタスクをキャンセルする。

## Objective-C Declaration
```objective-c
- (void)cancel;
```

## Discussion
`API::DataTask::cancel` を呼び出し、delegate を `nil` に戻す。

## References
- [`_WKDataTask.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.h#L44)
- [`_WKDataTask.mm#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L131)
- [`_WKDataTask.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L133)
- [`_WKDataTask.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |

# ``WKInternalsNotes/_WKDataTask/delegate``

データタスクの delegate を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) id <_WKDataTaskDelegate> delegate;
```

## Default Value
生成直後は `nil`。タスクのキャンセルや完了時に `nil` に戻される。

## Discussion
setter は `_delegate` を更新し、`WKDataTaskClient` を生成して `API::DataTask` の client に設定する。`didCompleteWithError` と `cancel` で delegate を `nil` に戻す。

## References
- [`_WKDataTask.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.h#L40)
- [`_WKDataTask.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.h#L42)
- [`_WKDataTask.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L117)
- [`_WKDataTask.mm#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L131)
- [`_WKDataTask.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L150)
- [`_WKDataTask.mm#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L152)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |

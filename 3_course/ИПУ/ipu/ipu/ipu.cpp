#include "lusb0_usb.h" // Подключаем библиотеки
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <conio.h>
#include <Windows.h>
#include <stdlib.h>

using namespace std;

void print_device_desc(struct usb_device_descriptor* device)	// Функция для вывода дескрипторов устройства
{
	// С помощью этой функции на экран выводятся названия дескрипторов устройства и непосредственно дескрипторы
	cout << left << setw(24) << dec << "  bLength: " << int(device->bLength) << endl;
	cout << left << hex << setw(24) << "  bDescriptorType: " << int(device->bDescriptorType) << "h" << endl;
	cout << left << hex << setw(24) << "  bcdUSB: " << int(device->bcdUSB) << "h" << endl;
	cout << left << hex << setw(24) << "  bDeviceClass: " << int(device->bDeviceClass) << "h" << endl;
	cout << left << hex << setw(24) << "  bDeviceSubClass: " << int(device->bDeviceSubClass) << "h" << endl;
	cout << left << hex << setw(24) << "  bDeviceProtocol: " << int(device->bDeviceProtocol) << "h" << endl;
	cout << left << hex << setw(24) << "  bMaxPacketSize0: " << int(device->bMaxPacketSize0) << "h" << endl;
	cout << left << hex << setw(24) << "  idVendor: " << int(device->idVendor) << "h" << endl;
	cout << left << hex << setw(24) << "  idProduct: " << int(device->idProduct) << "h" << endl;
	cout << left << hex << setw(24) << "  bcdDevice: " << int(device->bcdDevice) << "h" << endl;

	return;
}

void print_config_desc(struct usb_config_descriptor *config)	// Функция для вывода дескрипторов конфигурации
{
	// С помощью этой функции на экран выводятся названия дескрипторов конфигурации и дескрипторы конфигурации USB-устройства
	cout << left << setw(27) << "    wTotalLength: " << config->wTotalLength << endl;
	cout << left << setw(27) << "    bNumInterfaces: " << int(config->bNumInterfaces) << endl;
	cout << left << setw(27) << "    bConfigurationValue: " << int(config->bConfigurationValue) << endl;
	cout << left << setw(27) << "    iConfiguration: " << int(config->iConfiguration) << endl;
	cout << left << setw(27) << hex << "    bmAttributes: " << int(config->bmAttributes) << "h" << endl;
	cout << left << setw(27) << "    MaxPower: " << int(config->MaxPower) << endl;

	return;
}

void print_interface_desc(struct usb_interface_descriptor* interface)	// Функция для вывода дескрипторов интерфейса
{
	/* С помощью этой функции на экран выводятся названия дескрипторов интерфейса и дескрипторы интерфейса для
	конкретной конфигурации USB-устройства */
	cout << left << setw(30) << "       bInterfaceNumber: " << int(interface->bInterfaceNumber) << endl;
	cout << left << setw(30) << "       bAlternateSetting: " << int(interface->bAlternateSetting) << endl;
	cout << left << setw(30) << "       bNumEndpoints: " << int(interface->bNumEndpoints) << endl;
	cout << left << setw(30) << "       bInterfaceClass: " << int(interface->bInterfaceClass) << endl;
	cout << left << setw(30) << "       bInterfaceSubClass: " << int(interface->bInterfaceSubClass) << endl;
	cout << left << setw(30) << "       bInterfaceProtocol: " << int(interface->bInterfaceProtocol) << endl;
	cout << left << setw(30) << "       iInterface: " << int(interface->iInterface) << endl;

	return;
}

void print_endpoint_desc(struct usb_endpoint_descriptor* endpoint)	// Функция для вывода дескрипторов конечной точки
{
	/* С помощью этой функции на экран выводятся названия дескрипторов конечной точки и дескрипторы конечной точки
	для выбранного интерфейса*/
	cout << left << setw(33) << hex << "          bEndpointAddress: " << int(endpoint->bEndpointAddress) << "h" << endl;
	cout << left << setw(33) << hex << "          bmAttributes: " << int(endpoint->bmAttributes) << "h" << endl;
	cout << left << setw(33) << "          wMaxPacketSize: " << int(endpoint->wMaxPacketSize) << endl;
	cout << left << setw(33) << "          bInterval: " << int(endpoint->bInterval) << endl;
	cout << left << setw(33) << "          bRefresh: " << int(endpoint->bRefresh) << endl;
	cout << left << setw(33) << "          bSynchAddress: " << int(endpoint->bSynchAddress) << endl << endl;

	return;
}

void print_device(struct usb_device *dev)	// Функция для работы с USB-устройством
{
	usb_dev_handle *udev;
	char string[256];
	udev = usb_open(dev);	// Открываем USB-устройство для работы
	if (udev == 0)	// Если не удалось открыть устройство, то получаем информацию об ошибке (почему не удалось открыть)
	{
		cout << "Can't open USB-device " << usb_strerror() << endl;
		return;
	}

	cout << hex << uppercase << "Device VID: " << dev->descriptor.idVendor << endl; // Выводим на экран VID

	cout << hex << uppercase << "Device PID: " << dev->descriptor.idProduct << endl; // и PID для устройства

	usb_get_string_simple(udev, dev->descriptor.iManufacturer, string, 256);	// Получаем и выводим на экран строковый дискриптор, который содержит информацию о производителе
	cout << "Manufacturer: " << string << endl;

	usb_get_string_simple(udev, dev->descriptor.iProduct, string, 256);	// Получаем и выводим на экран строковый дискриптор, который содержит информацию о продукте
	cout << "Product: " << string << endl;

	usb_get_string_simple(udev, dev->descriptor.iSerialNumber, string, sizeof(string));	// Получаем и выводим на экран строковый дискриптор, который содержит информацию о серийном номере устройства
	cout << "Serial Number: " << string << endl;

	print_device_desc(&dev->descriptor);	// Вызываем функцию, которая будет выводить на экран дескрипторы устройства

	for (int i = 0; i < int(dev->descriptor.bNumConfigurations); i++)	// В этом цикле вызываем функцию каждый раз, когда находим новую конфигурацию устройства
	{
		print_config_desc(&dev->config[i]);	// Функция, которая выводит дескрипторы для каждой конфигурации
	}

	for (int i = 0; i < int(dev->config->bNumInterfaces); i++)	// В этом цикле вызываем функцию каждый раз, когда находим новый интерфейс для конкретной конфигурации устройства
	{
		print_interface_desc(&dev->config->interface->altsetting[i]);	// Функция, которая выводит дескрипторы для каждого интерфейса в конфигурации
	}

	for (int i = 0; i < int(dev->config->interface->altsetting->bNumEndpoints); i++)	// В этом цикле вызываем функцию каждый раз, когда находим новую конечную точку в интерфейсе устройства
	{
		print_endpoint_desc(&dev->config->interface->altsetting->endpoint[i]);	// Функция, которая выводит дескрипторы для каждой конечной точки в интерфейсе
	}

	return;
}

int main()	// Основная функция
{

	while (true)	// Бесконечный цикл, который нужен для динамического обновления информации об активных USB-устройствах
	{
		int chet = 0;	// Вводим 2 счетчика устройств
		int chet2 = 0;
		usb_init();	// Инициализируем USB-устройство
		usb_find_busses();	// Находим все шины USB
		usb_find_devices();	// Находим USB-устройства, которые расположены на шинах
		usb_bus *bus;
		for (bus = usb_busses; bus; bus = bus->next)	// Проходим по всем шинам
		{

			struct usb_device *dev;
			for (dev = bus->devices; dev; dev = dev->next)	// Перебираем все устройства на каждой найденной шине
			{
				chet++;	// Увеличиваем счетчик устройств на 1
				print_device(dev);	// Вызываем функцию, которая будет выводить дескрипторы USB-устройства (в этой функции будут вызываться функции для вывода других характеристик устройства)
				cout << "/-------------------------------------------/\n" << endl;
			}
		}
		chet2 = chet;
		while (chet == chet2)	// В этом цикле проверяем не изменилось ли количество устройств
		{
			chet2 = 0;
			usb_init();
			usb_find_busses();
			usb_find_devices();
			usb_bus *bus;
			for (bus = usb_busses; bus; bus = bus->next)
			{
				struct usb_device *dev;
				for (dev = bus->devices; dev; dev = dev->next)
				{
					chet2++;	// Увеличиваем счетчик USB-устройств на 1
				}
			}
		}
		system("cls");
	}
	system("pause");
	return 0;
}